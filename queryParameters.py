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

