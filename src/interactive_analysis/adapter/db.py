from __future__ import annotations
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
from functools import lru_cache
# Create SqlAlchemy engine of Postgres database

from ..port.model import AnalysisConfig


class PostgresEngine:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.engine = create_engine(connection_string)

    def create_session(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def get_engine(self):
        return self.engine

    @classmethod
    def get_postgres_engine(cls, env_var_name: str) -> PostgresEngine:
        """ get postgres engine from config file

        Returns:
            _type_: _description_
        """
        analysis_config: AnalysisConfig = AnalysisConfig.create_from_json(
            os.getenv('ANALYSIS_CONFIG_PATH')
        )

        connection_string = getattr(analysis_config, env_var_name)
        return cls(connection_string=connection_string)


def create_conn_engine(connection_string: str):
    """ Create connection to database

    Args:
        connection_string (str): e.g. postgresql://postgres:postgres@localhost:5432/interactive_analysis

    Returns:
        _type_: _description_
    """
    engine = create_engine(
        connection_string=connection_string,)
    return engine

# Create SqlAlchemy session


def create_session(engine):
    """ Create session to database

    Args:
        engine (_type_): _description_

    Returns:
        _type_: _description_
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
