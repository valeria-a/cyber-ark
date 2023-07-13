import datetime
import math
import os.path
import time
import uuid

import aiofiles
import uvicorn
from fastapi import FastAPI, UploadFile
from pydantic import BaseModel, Field

from meeting3.tasks_mngr import TasksMngr

app = FastAPI()

task_mngr = TasksMngr()

class MyRequestData(BaseModel):
    id: int = Field(gt=0)
    name: str
    birth_date: datetime.date

class MyResponse(BaseModel):
    answer: str




@app.post("/api/upload")
async def upload(file: UploadFile):
    # whole file
    print(f"Starting upload", file)
    task_id = str(uuid.uuid4())
    out_file_path = f"temp/{task_id}-{file.filename}"

    if not os.path.exists("temp/"):
        os.makedirs("temp/")

    # async with aiofiles.open(out_file_path, 'wb') as out_file:
    #     content = await file.read()  # async read
    #     await out_file.write(content)  # async write
    # in chunks
    async with aiofiles.open(out_file_path, 'wb') as out_file:
        while content := await file.read(1024):  # async read chunk
            await out_file.write(content)  # async write chunk
    # p = Popen(cmd, stdout=PIPE, bufsize=0)
    # await p.wait() # 30 mins

    # non blocking
    task = task_mngr.run_conversion(out_file_path, task_id)
    return task

@app.get("/api/status")
async def status(task_id: str):
    print(task_id)
    return task_mngr.get_task_status(task_id)

@app.get("/api/cancel")
async def cancel(task_id: str):
    print(task_id)
    task_mngr.cancel_task(task_id)
    return {'status': 'cancelling'}

@app.post("/api/answer_me")
async def answer_me(request_data: MyRequestData):
    print(request_data)
    return MyResponse(answer=f"Hello {request_data.name}")

@app.get("/api/hello")
async def hello():
    return {'word': 'hello'}

@app.get("/api/long")
async def long():
    # long calculation
    time.sleep(10)
    return {'word': 'long'}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)