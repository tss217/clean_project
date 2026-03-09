from sqlalchemy import create_engine

class DBConnectionHaandler:
    def __init__(self) -> None:
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format("mysql+pymysql","root","123456","localhost","3306","clean_databse")
        self.__engine = self.__creat_database_engine()

    def __creat_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    
    def get_engine(self):
        return self.__engine