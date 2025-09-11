from fastapi import FastAPI, Path, Query, Body
from typing import Annotated
from pydantic import BaseModel

app=FastAPI()

class Item(BaseModel):
    name: str
    description:str|None=None
    value:float
    tax:float|None=None

class User(BaseModel):
    username:str
    full_name:str|None=None

@app.put("/items/{item_id}")
async def put_item(
    item_id:Annotated[int, Path(description="Hello, World!", ge=0, le=1000 )],
    importance:Annotated[int, Body(alias="import")],
    q:Annotated[str|None, Query(alias="qparam")]=None,
    item:Item|None=None,
    user:User|None=None,
):
    result={"Item_id":item_id, "importance":importance}
    if q:
        result.update({"q":q})
    if item:
        result.update({"item":item})
    if user:
        result.update({"User":user})
    if importance:
        result.update({"importance":importance})
    return result