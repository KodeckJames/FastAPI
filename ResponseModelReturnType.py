from fastapi import FastAPI, Body
from pydantic import BaseModel, EmailStr
from typing import Annotated

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
async def get_item()->any:
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

@app.post("/user/", response_model=UserOut)
async def get_user(user:Annotated[UserIn, Body()])->any:
    return user