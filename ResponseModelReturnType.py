from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Annotated

app=FastAPI()

class Item(BaseModel):
    name:str
    description:str|None=None
    price:float
    tax:float|None=None
    needs:list[str]=[]

@app.post("/items")
async def create_item(item:Annotated[Item, Body(embed=True)]) -> Item:
    return item

@app.get("/items")
async def read_item()->list[Item]:
    return [
        Item(name="Yellow", price=54.89),
        Item(name="YesYes", price=87.23)
    ]

# Without -> Item: still works ✔️

# With -> Item:
# ✅ Better docs
# ✅ Automatic response validation
# ✅ Easier development (type hints, autocompletion)

# It’s less about “making the API work” and more about “making it robust, safe, and well-documented.”