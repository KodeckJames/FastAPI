from fastapi import FastAPI, Path, Query
from typing import Annotated

app=FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id:Annotated[int, Path(title="This is the title of the Path Parameter")], q:Annotated[str|None, Query(alias="query-param")]=None):
    results={"item_id":item_id}
    if q:
        results.update({"q":q})
    return results

#Number validations: greater than or equal
@app.get("/numvalidation/{item_id}")
async def read_item(item_id:Annotated[int, Path(title="Item ID", ge=10)], q:str):
    results={"item_id":item_id}
    if q:
        results.update({"q":q})
    return results

#Number validations: greater than and less than or equal
@app.get("/numvalidations2/{item_id}")
async def read_item(item_id:Annotated[int, Path(gt=0, le=1000)], q: str):
    results={"item_id":item_id}
    if q:
        results.update({"q":q})
    return results