from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Item(BaseModel):
    name: str
    item: str
    price: float
    description: str | None = None
    tax: float | None = None

@app.post("/items/")
async def post_item(item: Item):
    return item