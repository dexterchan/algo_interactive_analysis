from __future__ import annotations
from abc import ABCMeta, abstractmethod
import numpy as np
from .indicators import (
    calculate_log_price_change,
    calculate_simple_moving_average,
    calculate_rsi,
)
import pandas as pd


class Feature(metaclass=ABCMeta):
    """feature class"""

    @abstractmethod
    def output_feature_array(self) -> np.ndarray:
        """output array

        Returns:
            np.ndarray: array
        """
        pass


class Log_Price_Feature(Feature):
    """log price feature class"""

    def __init__(self, df_price: pd.Series, dimension: int):
        """initialize log price feature class

        Args:
            df_price (pd.Series): price series
            dimension (int): dimension of the feature
        """
        self.df_price = df_price
        self.dimension = dimension

    def _calculate(self) -> pd.Series:
        """helper function calculate log price change from pandas series

        Returns:
            pd.Series: log price change
        """
        log_price_change = calculate_log_price_change(self.df_price)
        # drop nan
        log_price_change = log_price_change.dropna()
        return log_price_change

    def output_feature_array(self) -> np.ndarray:
        """output array

        Returns:
            np.ndarray: array
        """
        log_price_raw = self._calculate()

        # Constract feature array of (N-dimension) x (dimension)
        log_price_feature_array = np.zeros(
            (len(log_price_raw) - self.dimension, self.dimension)
        )
        for i in range(self.dimension):
            log_price_feature_array[:, i] = log_price_raw[
                i : i + len(log_price_raw) - self.dimension
            ].values

        return log_price_feature_array

    def shape(self) -> tuple:
        """shape of the feature array

        Returns:
            tuple: shape of the feature array
        """
        return len(self.df_price) - 1 - self.dimension, self.dimension


class SMA_Cross_Feature(Feature):
    """calculate the cross of two SMA signals

    Args:
        Feature (_type_): _description_
    """

    def __init__(
        self, df_price: pd.Series, sma_window_1: int, sma_window_2: int, dimension: int
    ) -> None:
        self.df_price = df_price
        self.sma_window_1 = sma_window_1
        self.sma_window_2 = sma_window_2
        self.dimension = dimension

    def _calculate(self) -> pd.Series:
        """calculate the cross over of two SMA signals

        Returns:
            pd.Series: Cross over signals of two SMA
        """
        sma_1 = calculate_simple_moving_average(self.df_price, self.sma_window_1)
        sma_2 = calculate_simple_moving_average(self.df_price, self.sma_window_2)

        sma_cross = self._cross_over_lineA_above_lineB(sma_1, sma_2)
        # drop nan
        sma_cross.dropna(inplace=True)
        return sma_cross

    def _cross_over_lineA_above_lineB(
        self, lineA: pd.Series, lineB: pd.Series
    ) -> pd.Series:
        """calculate the cross over of two lines:
            lineA cross above lineB
            it output True/False if there is lineA crossing above linB signal

        Args:
            lineA (pd.Series): pandas Series column with numeric type
            lineB (pd.Series): pandas Series column with numeric type

        Returns:
            pd.Series: Series of True or False
        """
        lineA_minus_lineB = lineA - lineB
        prev_lineA_minus_lineB = lineA_minus_lineB.shift(1)

        return np.where(
            ((lineA_minus_lineB > 0) & (prev_lineA_minus_lineB < 0)), True, False
        )

    def output_feature_array(self) -> np.ndarray:
        """output array

        Returns:
            np.ndarray: array
        """
        # Constract feature array of (N-dimension) x (dimension)
        sma_cross = self._calculate()
        sma_cross_feature_array = np.zeros(
            (len(sma_cross) - self.dimension, self.dimension)
        )
        for i in range(self.dimension):
            sma_cross_feature_array[:, i] = sma_cross[
                i : i + len(sma_cross) - self.dimension
            ].values

        return sma_cross_feature_array

    def shape(self) -> tuple:
        """shape of the feature array

        Returns:
            tuple: shape of the feature array
        """
        invalid_data_length = max(self.sma_window_1, self.sma_window_2) - 1
        return len(self.df_price) - invalid_data_length - self.dimension, self.dimension
