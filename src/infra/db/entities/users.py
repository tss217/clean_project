from pickle import TRUE

from sqlalchemy import Column, PrimaryKeyConstraint, String, Integer, column
from src.infra.db.base import Base

class Users(Base):
    __tablename__ = "users"

    id = Column (Integer, primary_key = True, autoincrement = True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable= False)

    def __repr__(self):
        return f"Users [id = {self.id}, first_name ={self.first_name}]"
