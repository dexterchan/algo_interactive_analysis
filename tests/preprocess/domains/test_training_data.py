from preprocess_data.domains.training_data import splitting_training_and_eval_time_range
from datetime import datetime, timedelta
from preprocess_data.logging import get_logger

logger = get_logger(__name__)


def test_splitting_training_and_eval_time_range() -> None:
    num_of_data_vector = 10
    start_date = datetime(2021, 1, 1)
    end_date = start_date + timedelta(days=7 * num_of_data_vector)
    data_length = timedelta(days=7)
    split_ratio = 0.8

    (training_time_range, eval_time_range) = splitting_training_and_eval_time_range(
        start_date=start_date,
        end_date=end_date,
        data_length=data_length,
        split_ratio=split_ratio,
    )
    num_training_vector = int(num_of_data_vector * split_ratio)
    assert len(training_time_range) == num_training_vector
    assert len(eval_time_range) == num_of_data_vector - num_training_vector

    pass
