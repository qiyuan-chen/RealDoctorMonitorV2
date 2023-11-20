from typing import Optional

from fastapi import FastAPI


app = FastAPI()


@app.post("/receive_info")
async def receive_info(info: Optional[str] = None):
    # Save the info to a database or a file
    with open("info.txt", "a") as f:
        f.write(info + "\n")
    return {"status": "info received"}
