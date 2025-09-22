from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Union

app=FastAPI()

class UserIn(BaseModel):
    username:str
    password:str
    email:EmailStr
    full_name:str|None=None

class UserOut(BaseModel):
    username:str
    email:EmailStr
    full_name:str|None=None

class UserInDB(BaseModel):
    username:str
    hashed_password:str
    email:EmailStr
    full_name:str|None=None

def fake_password_hasher(raw_password:str):
    return (f"Super Secret: {raw_password}")

def fake_save_user(user_in:UserIn):
    hashed_password=fake_password_hasher(user_in.password)
    user_in_db=UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    print("User saved!... not really")
    return user_in_db

@app.post("/user/", response_model=UserOut)
async def create_user(user_in:UserIn):
    user_saved=fake_save_user(user_in)
    return user_saved

# Reducing duplication using class inheritance
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str

def fake_password_hasher(raw_password:str):
    return (f"Super Secret: {raw_password}")

def fake_save_user(user_in:UserIn):
    hashed_password=fake_password_hasher(user_in.password)
    user_in_db=UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    print("User saved!... not really")
    return user_in_db

@app.post("/user/", response_model=UserOut)
async def create_user(user_in:UserIn):
    user_saved=fake_save_user(user_in)
    return user_saved

# Union or anyOf
class ItemType(BaseModel):
    description:str
    type:str

class CarItem(ItemType):
    type:str="Car"

class PlaneType(ItemType):
    type:str="Plane"
    size:int

items={
    "item1":{"description":"This is a car","type":"GLE"},
    "item2":{"description":"This is a plane","type":"Airbus","size":8}
}

@app.get("/items/{item_id}", response_model=Union[PlaneType, CarItem])
async def get_item(item_id:str):
    return items[item_id]

# In this example we pass Union[PlaneItem, CarItem] as the value of the argument response_model.
# Because we are passing it as a value to an argument instead of putting it in a type annotation, we have to use Union even in Python 3.10.
# If it was in a type annotation we could have used the vertical bar, as:
# some_variable: PlaneItem | CarItem
# But if we put that in the assignment response_model=PlaneItem | CarItem we would get an error, because Python would try to perform an invalid operation between PlaneItem and CarItem instead of interpreting that as a type annotation.

# Returning a list as response:
class ListItems(BaseModel):
    name:str
    description:str

item_list=[
    {"name":"Jlow","description":"He is a good fella"},
    {"name":"JJ","description":"He is a respectable member of the society"}
]

@app.get("/itemList", response_model=list[ListItems])
async def get_listItem():
    return item_list