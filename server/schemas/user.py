from pydantic import BaseModel, EmailStr


# 用于接收用户输入的模型
class UserLogin(BaseModel):
    username: str
    password: str


class UserCreate(BaseModel):
    username: str
    password: str
    email: EmailStr


# 用于返回给用户的模型，不返回密码


class UserOut(BaseModel):
    username: str
    role: str
    email: EmailStr

    class Config:
        orm_mode = True
