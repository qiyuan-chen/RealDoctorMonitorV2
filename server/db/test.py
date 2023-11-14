from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+aiomysql://root:cqy20011012@localhost/RealDoctorMonitor"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建一个Base类，后续的模型会继承这个类
Base = declarative_base()


session = SessionLocal()


print(session.query(text("select * from Users")).all())

session.close()
