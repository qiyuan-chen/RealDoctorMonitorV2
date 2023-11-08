from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from ..db.database import SessionLocal
from ..db.models import User
from ..schemas.user import UserCreate, UserOut
from ..utils import verify_password

router = APIRouter()


# 依赖项
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/login", response_model=UserOut)
async def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return db_user
