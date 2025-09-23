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

# Optional file upload and also add metadata
@app.post("/optionalFile/")
async def optional(userOptional:Annotated[bytes|None, File(description="This is an optional file upload API")]=None):
    if userOptional:
        return{"FileLength":len(userOptional)}
    return{"Message":"No file uploaded"}

@app.post("/optionalUploadFile/")
async def optional2(myfileOptional:Annotated[UploadFile|None, File(description="This is an optional file upload API")]=None):
    if myfileOptional:
        return{"Name":myfileOptional.filename}
    return{"Message":"No file uploaded"}
