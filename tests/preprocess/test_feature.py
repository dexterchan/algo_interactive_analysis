from __future__ import annotations
from preprocess_data.port.interfaces import (
    Feature_Definition, 
    RSI_Feature_Interface, 
    Log_Price_Feature_Interface,
    SMA_Cross_Feature_Interface,
    Feature_Enum, 
)
from preprocess_data.port.features import create_feature_from_close_price
import pytest

@pytest.fixture()
def get_feature_spec() -> list[Feature_Definition]:
    
    LOOK_BACK:int = 3
    feature_definitions = [
        Feature_Definition(
            meta={"name":Feature_Enum.LOG_PRICE},
            data=Log_Price_Feature_Interface(
                dimension = LOOK_BACK
            )
        ),
        Feature_Definition(
            meta={"name": Feature_Enum.RSI},
            data=RSI_Feature_Interface(
                rsi_window=14,
                dimension=LOOK_BACK
            )
        ),
        Feature_Definition(
            meta={"name": Feature_Enum.SMA_CROSS},
            data=SMA_Cross_Feature_Interface(
                sma_window_1=20,
                sma_window_2=50,
                dimension=LOOK_BACK
            )
        )
    ]
    return feature_definitions

def test_feature_preparation(get_test_decending_then_ascending_mkt_data, get_feature_spec) -> None:
    candles = get_test_decending_then_ascending_mkt_data(dim=100)

    feature_array = create_feature_from_close_price(
        ohlcv_candles=candles,
        feature_pools=get_feature_spec
    )
    pass