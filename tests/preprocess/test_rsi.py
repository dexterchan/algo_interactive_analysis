from __future__ import annotations

from preprocess_data.domains.features_gen import RSI_Feature
from preprocess_data.domains.indicators import calculate_rsi

import numpy as np
import pytest
import logging
import pandas as pd

logger = logging.getLogger(__name__)


TOLERANCE: float = 0.0001
LOOK_BACK: int = 3


def test_rsi_indicator(get_test_decending_then_ascending_mkt_data) -> None:
    dim: int = 100
    rsi_window: int = 14
    mktdata_close = get_test_decending_then_ascending_mkt_data(dim=dim)["close"]

    raw_rsi = calculate_rsi(df_price=mktdata_close, window=rsi_window)
    raw_rsi.dropna(inplace=True)
    assert len(raw_rsi) == len(mktdata_close) - rsi_window
    pass


def test_rsi_feature(get_test_decending_then_ascending_mkt_data) -> None:
    dim: int = 100
    rsi_window: int = 14
    mktdata_close = get_test_decending_then_ascending_mkt_data(dim=dim)["close"]

    rsi_feature = RSI_Feature(
        df_price=mktdata_close, dimension=LOOK_BACK, rsi_window=rsi_window
    )

    feature_array = rsi_feature.output_feature_array()

    assert len(feature_array) == len(mktdata_close) - LOOK_BACK - rsi_window
    pass
