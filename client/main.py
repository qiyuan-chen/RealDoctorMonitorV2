import requests
from fastapi import FastAPI

from setting import Settings

app = FastAPI()
settings = Settings()


@app.get("/send_info")
async def send_info():
    data = {"info": "This is some information"}
    response = requests.post("http://{}/receive_info".format(settings.server_host), json=data)
    return {"status": "info sent"}


