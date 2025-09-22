# WHen you need to receive form fields instead of JSON, you can use Form but first you need to install python-multipart

from fastapi import FastAPI, Form
from typing import Annotated

app=FastAPI()

@app.post("/users/")
async def user_details(name:Annotated[str, Form()], password:Annotated[str, Form()]):
    return {"Name":name}