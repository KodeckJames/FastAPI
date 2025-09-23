from fastapi import FastAPI, Form
from typing import Annotated
from pydantic import BaseModel, EmailStr

app=FastAPI()

class UserModel(BaseModel):
    username:str
    email:EmailStr


@app.post("/formUser/")
async def get_user_details(user_details:Annotated[UserModel, Form()]):
    return user_details
