from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Item(BaseModel):
    name:str
    description:str|None=None
    price:float
    tax:float|None=None
    prizes:list[str]=[]
    tags:set[str]=()

@app.put("/item/{item_id}")
async def put_item(item_id:int, item:Item):
    result={"item_id":item_id, "item":item}
    return result