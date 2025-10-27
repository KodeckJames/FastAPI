from typing import Annotated
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer

app=FastAPI()

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="token")

@app.get("/index")
async def read_items(token:Annotated[str, Depends(oauth2_scheme)]):
    return{"Token":token}