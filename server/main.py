from fastapi import FastAPI

from .db.database import database
from .routes import user as user_routes

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# 包含路由
app.include_router(user_routes.router)

# 以这种方式启动应用：`uvicorn main:app --reload`
