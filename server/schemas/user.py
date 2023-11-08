from pydantic import BaseModel


# 用于接收用户输入的模型
class UserCreate(BaseModel):
    username: str
    password: str


# 用于返回给用户的模型，不返回密码
class UserOut(BaseModel):
    username: str

    class Config:
        orm_mode = True
