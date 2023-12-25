from unittest import result
import requests
from fastapi import FastAPI

app = FastAPI()

server_host = ""


from gpu import get_gpu_usage_info, get_every_gpu_usage


@app.get("/send_info")
async def send_info():
    result = get_gpu_usage_info()
    data = get_every_gpu_usage(result)
    response = requests.post("http://{}/receive_info".format(server_host), json=data)
    return {"status": "info sent"}

# 测试函数
@app.get("/test")
async def send_info():
    result = get_gpu_usage_info()
    data = get_every_gpu_usage(result)
    return data
    

    
# 启动服务器
# uvicorn main:app --reload --host


