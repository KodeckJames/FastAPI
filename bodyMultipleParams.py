from fastapi import FastAPI, Path, Query
from typing import Annotated
from pydantic import BaseModel

app=FastAPI()

class Item(BaseModel):
    name: str
    description:str|None=None
    value:float
    tax:float|None=None

@app.put("/items/{item_id}")
async def put_item(
    item_id:Annotated[int, Path(description="Hello, World!", ge=0, le=1000 )],
    q:Annotated[str|None, Query(alias="qparam")]=None,
    item:Item|None=None
):
    result={"Item_id":item_id}
    if q:
        result.update({"q":q})
    if item:
        result.update({"item":item})
    return result