from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(120))
    role = Column(String(30))
    hashed_password = Column(String(100))


# Use a synchronous database URL
DATABASE_URL = "mysql+pymysql://root:cqy20011012@localhost/RealDoctorMonitor"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

db = SessionLocal()
users = db.query(User).all()
for user in users:
    print(user.username)