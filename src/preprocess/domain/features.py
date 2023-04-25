from abc import ABCMeta, abstractmethod
import numpy as np
from .indicators import calculate_log_price_change
import pandas as pd

class Feature(metaclass=ABCMeta):
    """ feature class
    """

    @abstractmethod
    def output_feature_array(self) -> np.ndarray:
        """ output array

        Returns:
            np.ndarray: array
        """
        pass

    

class log_price_feature(Feature):
    """ log price feature class
    """
    def __init__(self, df_price:pd.Series, dimension:int):
        """ initialize log price feature class

        Args:
            df_price (pd.Series): price series
            dimension (int): dimension of the feature
        """
        self.df_price = df_price
        self.dimension = dimension

    def _calculate(self) -> pd.Series:
        """ helper function calculate log price change from pandas series

        Returns:
            pd.Series: log price change
        """
        log_price_change = calculate_log_price_change(self.df_price)
        # drop nan
        log_price_change = log_price_change.dropna()
        return log_price_change
    
    def output_feature_array(self) -> np.ndarray:
        """ output array

        Returns:
            np.ndarray: array
        """
        log_price_raw = self._calculate()
        
        # Constract feature array of (N-dimension) x (dimension)
        log_price_feature_array = np.zeros((len(log_price_raw)-self.dimension, self.dimension))
        for i in range(self.dimension):
            log_price_feature_array[:,i] = log_price_raw[i:i+len(log_price_raw)-self.dimension].values
        
        return log_price_feature_array
    
    def shape(self) -> tuple:
        """ shape of the feature array

        Returns:
            tuple: shape of the feature array
        """
        return len(self.df_price)-1-self.dimension, self.dimension
    
