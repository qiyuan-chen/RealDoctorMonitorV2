from fastapi import APIRouter, Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..db.database import SessionLocal
from ..db.models import User
from ..schemas.user import UserCreate, UserOut, UserLogin
from ..utils import verify_password, get_password_hash

router = APIRouter()


# 依赖项
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/login", response_model=UserOut)
async def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="用户不存在！")
    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="密码错误！")
    if db_user.role == "init":
        raise HTTPException(status_code=402, detail="首次登录，请修改密码和邮箱！")

    return db_user


@router.post("/register", response_model=UserOut)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    hashed_password = get_password_hash(user.password)
    db_user = User()
    db_user.username = user.username
    db_user.email = user.email
    db_user.hashed_password = hashed_password
    db_user.role = "user"
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
