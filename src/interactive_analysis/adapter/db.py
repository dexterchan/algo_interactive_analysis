
# Create SqlAlchemy engine of Postgres database
def create_engine(connection_string: str):
    """ Create connection to database

    Args:
        connection_string (str): e.g. postgresql://postgres:postgres@localhost:5432/interactive_analysis

    Returns:
        _type_: _description_
    """
    engine = create_engine(
        connection_string=connection_string,)
    return engine


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn
