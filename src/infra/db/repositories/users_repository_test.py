import pytest
from sqlalchemy import text
from src.infra.db.settings import conection
from src.infra.db.settings.conection import DBConnectionHaandler
from .users_repository import UsersRepository
from src.infra.db.repositories import users_repository


db_connection = DBConnectionHaandler()
connection = db_connection.get_engine().connect()


@pytest.mark.skip(reason="Sensitive test")
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

@pytest.mark.skip(reason="Sensitive test")
def test_select_users():
    mocked_firts_name = "ts"
    mocked_last_name = "217"
    mocked_age = 222

    sql = """INSERT INTO users (first_name, last_name, age) VALUES ('{}','{}','{}')""".format(mocked_firts_name,mocked_last_name,mocked_age)
    connection.execute(text(sql))
    connection.commit()

    users_repository = UsersRepository()
    response = users_repository.select_user(mocked_firts_name)

    assert response[0].first_name == mocked_firts_name
    assert response[0].last_name == mocked_last_name
    assert response[0].age == mocked_age

    connection.execute(text(f"""DELETE FROM users WHERE id = {response[0].id}"""))
    connection.commit()
