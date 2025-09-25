from fastapi import FastAPI, HTTPException, Path, Request
from typing import Annotated
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from fastapi.exception_handlers import (
    http_exception_handler, 
    request_validation_exception_handler
)

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

@app.get("/items2/{name_passed}")
async def raise_exception(name_passed:str):
    if name_passed=="yellow":
        raise UnicornException(name=name_passed)
    return {"name":name_passed}

# Override the default exception handlers
# Override request validation exceptions
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)

@app.get("/items3/{item_id}")
async def get_item(item_id:int):
    if item_id==3:
        raise HTTPException(status_code=418, detail="Nope, 3 is not the number")
    return{"Item_id":item_id}

# Use the RequestValidationError body
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc:RequestValidationError):
    return JSONResponse(status_code=422, content=jsonable_encoder({"details":exc.errors(), "body":exc.body})),

class Item(BaseModel):
    title:str
    size:int

@app.post("/items4/")
async def create_item(item:Item):
    return item

# Reuse FastAPI's exception handlers
@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    print(f"OMG! An HTTP error!: {repr(exc)}")
    return await http_exception_handler(request, exc)

@app.exception_handler(RequestValidationError)
async def validatio_exception_handler(request, exc):
    print(f"OMG! The client sent invalid data!: {exc}")
    return await request_validation_exception_handler(request, exc)

@app.get("/items5/{item_id}")
async def read_item(item_id: int):
    if item_id==3:
        raise HTTPException(status_code=418, detail="Nah, 3 can't be the number")
    return {"item_id":item_id}