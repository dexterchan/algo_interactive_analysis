import pytest
import logging

logger = logging.getLogger(__name__)


@pytest.mark.skip(reason="Not implemented yet")
def test_load_pnl_result_recursive() -> None:
    from interactive_analysis.port.pnl_result import (
        read_pnl_result_recursive_opt_into_pandas,
    )

    df = read_pnl_result_recursive_opt_into_pandas()
    logger.info(df)
    assert df.shape[0] > 0
