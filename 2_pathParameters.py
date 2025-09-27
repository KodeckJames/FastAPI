from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return{"item_id":item_id}

@app.get("/users/me")
async def get_users():
    return {"User":"Ni mimi JJ"}

@app.get("/users/{user_id}")
async def get_user_by_id(user_id: int):
    return {"User":user_id}

#PRE DEFINED CLASSES
class ModelName(str, Enum):
    alexNet="alexNet"
    yolo="yolo"
    yellow="yellow"

@app.get("/fixed/{model_name}")
async def get_fixed_route(model_name:ModelName):
    if model_name is ModelName.alexNet:
        return{"route": model_name, "Message":"This is alexNet"}
    if model_name.value == "yellow":
        return{"route":model_name, "Message":"This is yellow"}
    return {"route":model_name, "message":"This is yolo"}

@app.get("/files/{pathName:path}")
async def long_path(pathName: str):
    return{"file_path":pathName}
# With this, you can define your path like: http://127.0.0.1:8000/files//home/johndoe/myfiles/yellow/tiangolo/yesyes