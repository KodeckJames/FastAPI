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
    *,
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

#Embed a single body parameter
#Let's say you only have a single item body parameter from a Pydantic model Item.
# By default, FastAPI will then expect its body directly.
# But if you want it to expect a JSON with a key item and inside of it the model contents, as it does when you declare extra body parameters, you can use the special Body parameter embed:
class Item_lite(BaseModel):
    name: str
    description:str|None=None
    value:float
    tax:float|None=None

@app.put("/itemz")
async def add_item(item:Annotated[Item_lite, Body(embed=True)]):
    result={"item":item}
    return result

# In this case FastAPI will expect a body like:
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
}

# instead of:
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}