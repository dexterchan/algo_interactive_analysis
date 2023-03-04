import pandas as pd

from ..adapter.db import PostgresEngine

"""Main module."""


def read_pnl_result_recursive_opt_into_pandas() -> pd.DataFrame:
    # Read from sql table pnl_result_recursive_opt into pandas dataframe
    postgres_engine: PostgresEngine = PostgresEngine.get_postgres_engine(
        env_var_name='pnl_result_conn_str')
    query = """select exchange,symbol,batch_id,data_key,pnl,max_drawdown, 
                mkt_start_epoch,mkt_end_epoch,
                pnl_result_json
                from pnl_result_recursive_opt"""
    df = pd.read_sql_query(sql=postgres_engine.format_query(query),
                           con=postgres_engine.get_connection())
    return df
