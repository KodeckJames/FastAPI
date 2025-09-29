# You can define files and form fields at the same time using File and Form

from fastapi import FastAPI, Form, UploadFile, File
from typing import Annotated

app=FastAPI()

@app.post("/filesandforms/")
async def get_data(
    myfile:Annotated[UploadFile, File()],
    myForm:Annotated[str, Form()],
    myOtherFile:Annotated[bytes, File()]
):
    return{
        "MyFileType":myfile.content_type,
        "MyForm":myForm,
        "MyOtherFile":len(myOtherFile)
    }