from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db.database import database, engine, Base
from .routes import user as user_routes

app = FastAPI()

# 添加跨域资源共享中间件，使得前端可以访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# 包含路由
app.include_router(user_routes.router)

# 以这种方式启动应用：`uvicorn server.main:app --reload`
