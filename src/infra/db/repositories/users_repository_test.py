from sqlalchemy import text
from src.infra.db.settings.conection import DBConnectionHaandler
from .users_repository import UsersRepository


db_connection = DBConnectionHaandler()
connection = db_connection.get_engine().connect()

def test_insert_user():
    mocked_firts_name = "firsasa"
    mocked_last_name = "laas"
    mocked_age = 222

    users_repository = UsersRepository()
    users_repository.insert_user(mocked_firts_name,mocked_last_name,mocked_age) 

    #verificando se o dados foi inserido na tabela

    sql = """SELECT * FROM users WHERE first_name = '{}' AND last_name = '{}' AND age = '{}'""".format(mocked_firts_name, mocked_last_name, mocked_age)


    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.first_name == mocked_firts_name
    assert registry.last_name == mocked_last_name
    assert registry.age == mocked_age

    connection.execute(text(f"""DELETE FROM users WHERE id = {registry.id}"""))
    connection.commit()

    print()
    print(registry)