# You can define files to be uploaded by the user using File
from fastapi import FastAPI, File, UploadFile
from typing import Annotated
from fastapi.responses import HTMLResponse

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

# Multiple file uploads
@app.post("/optionalMultipleFile/")
async def multiple_files(userListFiles:Annotated[list[bytes], File(description="This is a multiple file upload API")]):
   return {"File_Length":[len(file) for file in userListFiles]}

@app.post("/optionalMultipleUploadFile/")
async def multiple_files2(myfileList:Annotated[list[UploadFile], File(description="This is a multiple file upload API")]):
    return{"Name":[file.filename for file in myfileList]}
   
@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)