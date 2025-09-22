from fastapi import FastAPI, status, Query
from typing import Annotated

app=FastAPI()

@app.get("/items/", status_code=201)
async def get_item(name:str):
    return {"name":name}

# Shortcut to remember the status code names:
# You can use the convenience variables from fastapi.status
@app.get("/car/", status_code=status.HTTP_201_CREATED)
async def create_car(carName:Annotated[str, Query()]="GLE"):
    return {"Car_name":carName}