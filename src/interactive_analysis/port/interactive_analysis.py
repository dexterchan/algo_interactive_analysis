import pandas as pd

from ..adapter.db import create_conn_engine

"""Main module."""



def read_pnl_result_recursive_opt_into_pandas() -> pd.DataFrame:
    #Read from sql table pnl_result_recursive_opt into pandas dataframe
    engine = create_conn_engine(connection_string='postg resql://postgres:postgres@localhost:5432/interactive_analysis')
    df = pd.read_sql_table(table_name='pnl_result_recursive_opt', con=engine)
    return df