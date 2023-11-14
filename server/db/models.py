from sqlalchemy import Column, Integer, String

from .database import Base


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(120))
    role = Column(String(30))
    hashed_password = Column(String(100))
