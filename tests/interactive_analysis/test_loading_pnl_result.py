from interactive_analysis.port.pnl_result import read_pnl_result_recursive_opt_into_pandas

import logging
logger = logging.getLogger(__name__)


def test_load_pnl_result_recursive() -> None:
    df = read_pnl_result_recursive_opt_into_pandas()
    logger.info(df)
    assert df.shape[0] > 0
