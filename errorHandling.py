from fastapi import FastAPI, HTTPException, Path, Request
from typing import Annotated
from fastapi.responses import JSONResponse

app=FastAPI()

items={
    "car":"This is a Mercedes SUV called the GLE"
}

@app.get("/items/{item_id}")
async def get_item(item_id:Annotated[str, Path()]):
    if item_id not in items:
        raise HTTPException(detail={"Error":"This item doesn't exist"}, status_code=404, headers={"X-Error":"This is a not found error"})
    return items[item_id]

# Custom Exception handlers
class UnicornException(Exception):
    def __init__(self, name:str):
        self.name=name

@app.exception_handler(UnicornException)
async def custom_exception(request:Request, exc:UnicornException):
    return JSONResponse(
        status_code=418,
        content={"Message":f"Oops! {exc.name} is not available"}
    )

@app.get("/items2/{name}")
async def raise_exception(name:str):
    if name=="yellow":
        raise UnicornException(name=name)
    return {"name":name}