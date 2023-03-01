from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Create SqlAlchemy engine of Postgres database


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
