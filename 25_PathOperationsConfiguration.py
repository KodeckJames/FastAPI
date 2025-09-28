from fastapi import FastAPI, status
from pydantic import BaseModel

app=FastAPI()

# Response Status Code
class Item(BaseModel):
    name:str
    message:str|None=None
    price:int
    tax:float|None=None
    tags:set[str]=set()

@app.get("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item:Item):
    return item
