from sqlalchemy import Column, Integer, String

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(120))
    role = Column(String(30))
    hashed_password = Column(String(100))

    # 这里的 hashed_password 应该存储密码的哈希值
