from fastapi import FastAPI, Body, Response, Query, Path
from pydantic import BaseModel, EmailStr
from typing import Annotated, Any
from fastapi.responses import JSONResponse, RedirectResponse

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

# response_model decorator Parameter

@app.get("/itemsdec/", response_model=list[Item])
async def get_item()->Any:
    return  [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]

@app.post("/itemsdec/", response_model=Item)
async def post_item(item:Annotated[Item, Body()]):
    return item

# Returning the same input data
class UserIn(BaseModel):
    name:str
    password:str
    email:EmailStr
    full_name:str|None=None

@app.post("/user/")
async def get_user(user:Annotated[UserIn, Body()])->UserIn:
    return user

# Adding an output model
# Here, even though our path operation function is returning the same input user that contains the password, we declared the response_model to be our model UserOut, that doesn't include the password, So, FastAPI will take care of filtering out all the data that is not declared in the output model (using Pydantic):
class UserIn(BaseModel):
    name:str
    password:str
    email:EmailStr
    full_name:str|None=None

class UserOut(BaseModel):
    name:str
    email:EmailStr
    full_name:str|None=None

@app.post("/userpass/", response_model=UserOut)
async def get_user(user:Annotated[UserIn, Body()])->Any:
    return user

# Return type and data filtering
class BaseUser(BaseModel):
    name: str
    email: EmailStr
    full_name: str | None = None

class UserIn2(BaseUser):
    password:str

@app.post("/userpass2/")
async def post_item(user2:Annotated[UserIn2, Body()])->BaseUser:
    return user2

# OTHER RETURN TYPE ANNOTATIONS
# Return a response directly
@app.get("/portal")
async def new_dimension(teleport:Annotated[bool, Query()]=False)->Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"Yellow!":"Here is your new dimension"})

# Annotate a Response subclass
@app.get("/defaultportal")
async def default_dimension()->JSONResponse:
    return JSONResponse(content={"Yellowwz!!":"You belong here buddy, Nowhere to run!!!"})

# Invalid Return Type Annotations

# @app.get("/fails")
# async def get_portal(teleport: bool = False) -> Response | dict:
#     if teleport:
#         return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#     return {"message": "Here's your interdimensional portal."}

# This fails because the type annotation is not a Pydantic type and is not just a single Response class or subclass, it's a union (any of the two) between a Response and a dict.

# Disable Response Model
@app.get("/withoutvalidation", response_model=None)
async def get_item(teleport:Annotated[bool, Query()]=False)->Response|dict:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=1Kzqln4HozQ")
    return JSONResponse(content={"Yooh":"Guess who's staying here!!"})

# Response Model encoding parameters
class Cars(BaseModel):
    name:str
    description:str|None="A good car"
    price:float
    tax:float=500000.00
    competitors:list[str]=[]

cars={
        "Mercedes":{"name":"GLE","price":10000000.00},
        "Mazda":{"name":"CX-8","description":"A good SUV if you are on a budget","price":4000000.00,"tax":100000,"competitors":["Hyundai","Honda","Toyota"]},
        "Honda":{"name":"Hybrid","description":"A good car","price":4000000.00,"tax":500000.00,"competitors":["Hyundai","Honda","Toyota"]}
    }

@app.get("/cars/{item_id}", response_model=Cars, response_model_exclude_unset=True, response_model_exclude_defaults=True)
async def available_cars(item_id:Annotated[str, Path()]):
    return cars[item_id]

# response_model_include and response_model_exclude
@app.get("/cars/{item_id}/name", response_model=Cars, response_model_include={"name","description"})
async def available_cars(item_id:Annotated[str, Path()]):
    return cars[item_id]

@app.get("/cars/{item_id}/public", response_model=Cars, response_model_exclude={"tax"})
async def available_cars(item_id:Annotated[str, Path()]):
    return cars[item_id]