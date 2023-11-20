from databases import Database
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 此处的driver要使用pymysql，之前的aiomysql会报错
DATABASE_URL = "mysql+pymysql://qychen:011012@localhost/RealDoctorMonitor"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建一个Base类，后续的模型会继承这个类
Base = declarative_base()

# 创建一个Database实例，用于后续的异步数据库操作
database = Database(DATABASE_URL)
