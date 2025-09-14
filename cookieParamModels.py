from fastapi import FastAPI, Cookie
from typing import Annotated
from pydantic import BaseModel

app=FastAPI()

class Cookies(BaseModel):
    session_id:str
    fatebook_tracker:str|None=None
    googall_tracker:str|None=None

@app.get("/items/")
async def get_item(cookies:Annotated[Cookies, Cookie()]):
    return cookies