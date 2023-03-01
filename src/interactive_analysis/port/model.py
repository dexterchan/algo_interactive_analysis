from __future__ import annotations
from dataclasses import dataclass
import json

@dataclass
class AnalysisConfig:
    strategy_calculation_log_directory: str
    pnl_result_conn_str: str
    strategy_conn_str: str
    live_trade_signal_conn_str: str

    @classmethod
    def create_from_json(cls, json_file:str):
        """ create AnalysisConfig from json file

        Args:
            json_file (str): json file path
        """
        obj_dict = json.load(open(json_file, 'r'))
        return cls(**obj_dict)
        