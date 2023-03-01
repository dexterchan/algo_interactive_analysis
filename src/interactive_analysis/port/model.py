from dataclasses import dataclass


@dataclass
class AnalysisConfig:
    strategy_calculation_log_directory: str
    pnl_result_conn_str: str
    strategy_conn_str: str
    live_trade_signal_conn_str: str
