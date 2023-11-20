from fastapi import FastAPI
from pydantic import BaseSettings

class Settings(BaseSettings):
    server_host: str = "192.168.0.185"

    class Config:
        env_file = ".env"
