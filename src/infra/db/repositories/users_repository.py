from src.infra.db.settings.conection import DBConnectionHaandler
from src.infra.db.entities.users import Users as UsersEntity

class UsersRepository:
    @classmethod
    def insert_user(cls,first_name:str,last_name:str, age:int)->None:
        with DBConnectionHaandler() as databse:
            try:
                assert databse.session is not None
                new_registry = UsersEntity(first_name=first_name,last_name=last_name,age=age)
                databse.session.add(new_registry)
                databse.session.commit()

            except Exception as exception:
                assert databse.session is not None
                databse.session.rollback()
                raise exception