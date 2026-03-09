
from .conection import DBConnectionHaandler

def test_create_data_engine():
    db_connection_handle =  DBConnectionHaandler()
    engine = db_connection_handle.get_engine()

    assert engine is not None
