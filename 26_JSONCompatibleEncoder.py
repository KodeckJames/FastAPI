from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from datetime import datetime

app=FastAPI()

fake_DB={}

class Item(BaseModel):
    name:str
    description:str
    date:datetime

@app.put("/items/{id}")
async def update_item(item:Item, id:str):
    jsonable_converted_data=jsonable_encoder(item)
    fake_DB[id]=jsonable_converted_data
    return fake_DB[id]