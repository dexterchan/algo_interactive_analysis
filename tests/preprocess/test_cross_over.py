# testing for preprocess.domain.features.SMA_Cross_Feature
from preprocess_data.domains.features_gen import SMA_Cross_Feature
from preprocess_data.domains.indicators import calculate_simple_moving_average
import math

import logging

logger = logging.getLogger(__name__)


def test_sma_calcuation(get_test_ascending_mkt_data) -> None:
    length = 100
    close_price = get_test_ascending_mkt_data(dim=length)["close"]
    sma_10 = calculate_simple_moving_average(df_price=close_price, window=10)
    sma_10.dropna(inplace=True)
    assert len(sma_10) == len(close_price) - 10 + 1

    sma_20 = calculate_simple_moving_average(df_price=close_price, window=20)
    sma_20.dropna(inplace=True)
    assert len(sma_20) == len(close_price) - 20 + 1
