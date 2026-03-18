from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHaandler:
    def __init__(self) -> None:
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format("mysql+pymysql","root","123456","localhost","3306","clean_database")
        self.__engine = self.__creat_database_engine()
        self.session = None

    def __creat_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    
    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
    
    def __exit__(self, exc_type,exc_val, exc_tb):
        assert self.session is not None
        self.session.close()