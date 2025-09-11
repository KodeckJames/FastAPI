from fastapi import FastAPI, Body, Path
from pydantic import BaseModel, Field
from typing import Annotated

app=FastAPI()

class Item(BaseModel):
    name:str
    description:str=Field(default=None, description="This is the description attribute", max_length=50)
    price:float=Field(gt=1.0, description="Price attribute")
    tax:float|None=None

@app.put("/items/{item_id}")
async def put_item(item_id:Annotated[int, Path(gt=1, lt=1000)], item:Annotated[Item, Body(embed=True)]):
    result={"item_id":item_id, "item":item}
    return result