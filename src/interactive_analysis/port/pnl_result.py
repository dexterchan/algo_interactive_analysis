import pandas as pd

from ..adapter.db import PostgresEngine

"""Main module."""


def read_pnl_result_recursive_opt_into_pandas() -> pd.DataFrame:
    # Read from sql table pnl_result_recursive_opt into pandas dataframe
    postgres_engine: PostgresEngine = PostgresEngine.get_postgres_engine(
        env_var_name='pnl_result_conn_str')

    df = pd.read_sql_table(
        table_name='pnl_result_recursive_opt', con=postgres_engine.get_engine())
    return df
