# You can define files to be uploaded by the user using File
from fastapi import FastAPI, File, UploadFile
from typing import Annotated

app=FastAPI()

@app.post("/file/")
async def get_file(userFile:Annotated[bytes, File()]):
    return {"File size":len(userFile)}

@app.post("/uploadFile/")
async def upload_file(myfile:UploadFile):
    data = await myfile.read()
    return {"fileName":myfile.content_type}