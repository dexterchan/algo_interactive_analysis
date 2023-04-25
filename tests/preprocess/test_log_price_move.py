# testing for preprocess.domain.features.log_price_move.LogPriceMove
from preprocess_data.domains.features_gen import Log_Price_Feature
import math

import logging

logger = logging.getLogger(__name__)


def test_output_feature_array(get_test_ascending_mkt_data) -> None:
    df = get_test_ascending_mkt_data()
    dim: int = 3
    log_price_move = Log_Price_Feature(df["close"], dim)
    price_move = log_price_move._calculate()
    feature_array = log_price_move.output_feature_array()
    assert feature_array.shape == (len(df) - 1 - dim, dim)
    # Check if the first element is correct and within the tolerance 0.0001
    assert len(price_move) == len(df) - 1
    assert (price_move[0] - math.log(df["close"][1] / df["close"][0])) < 0.0001

    # Check if feature_array[0] is the same as price_move[0:dim]
    assert (feature_array[0] == price_move[0:dim]).all()
    # Enumerate each vector of feature_array and check if it is the same as price_move[i:i+dim]
    for i, v in enumerate(feature_array):
        assert (v == price_move[i : i + dim]).all()
    pass
