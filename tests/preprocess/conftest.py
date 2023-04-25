import pytest

import pandas as pd
from datetime import datetime, timedelta
import numpy as np
@pytest.fixture
def get_test_ascending_mkt_data() -> pd.DataFrame:
    def _get_data(dim: int = 10, step:int=100):
        # Generate pandas dataframe of timestamps records
        df = pd.DataFrame(
            data={
                "timestamp": pd.date_range(start=datetime.now(),
                periods=dim,freq=timedelta(hours=1)),
                "inx": np.arange(dim)
            })
        df.set_index("timestamp", inplace=True, drop=True)
        df["close"] = df["inx"] * step + 1000

        df["price_movement"] = df["close"].diff()
        return df
        pass

    return _get_data