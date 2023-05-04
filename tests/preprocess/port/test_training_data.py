from __future__ import annotations

from preprocess_data.logging import get_logger
from preprocess_data.port.training_data_parquet import (
    prepare_training_data_and_eval_from_parquet,
)
from datetime import datetime, timedelta

import pytest

logger = get_logger(__name__)

test_symbol = "ETHUSD"
test_exchange = "kraken"
test_data_dir = "notebooks/data"


def test_prepare_training_data_and_eval_from_parquet() -> None:
    start_date = datetime(2020, 1, 1)
    end_date = start_date + timedelta(days=7 * 200)
    data_length = timedelta(days=7)
    split_ratio = 0.8

    # output_folder should be data/training/YYYYMMDD
    output_folder = f"notebooks/data/training/{test_exchange}/{test_symbol}/{datetime.now().strftime('%Y%m%d')}"

    prepare_training_data_and_eval_from_parquet(
        exchange=test_exchange,
        symbol=test_symbol,
        data_type="parquet",
        data_directory=test_data_dir,
        start_date=start_date,
        end_date=end_date,
        data_length=data_length,
        split_ratio=split_ratio,
        output_folder=output_folder,
        candle_size="15Min",
        min_candle_population=int(4 * 24 * 7 * 0.8),
    )
