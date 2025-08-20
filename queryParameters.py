from fastapi import FastAPI

app=FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/query/")
async def queryParam(skip: int=0, limit: int=10):
    return fake_items_db[skip: skip+limit]

#Optional Parameters
from typing import Optional

@app.get("/items/{item_id}")
async def get_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id":item_id, "q":q}
    return {"item_id":item_id}

#Query Parameter type conversion
@app.get("/itemz/{item_id}")
async def read_item(item_id: str, q: str | None = None, r: bool = False):
    items = {"Item_id": item_id}
    if q:
        items.update({"q":q})
    if not r:
        items.update({"Test":"This is the test Query Parameter type conversion"})    
    return items

#Multiple path and Query parameters
@app.get("/users/{user_id}/itemu/{item_id}")
async def get_user_item(user_id: int, item_id: str, q: str | None = None, r: bool = False):
    item = {"user":user_id, "itemu":item_id}
    if q:
        item.update({"q":q})
    if not r:
        item.update({"r":"Hello my good people"})
    return item

#Required Query parameters
@app.get("/temz/{item_id}")
async def get_needy(item_id: str, needy: str):
    items=[{"item_id":item_id},{"needy":needy}]
    return items