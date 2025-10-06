from fastapi import FastAPI, Header, HTTPException, Depends, status
from typing import Annotated

async def verify_token(q:Annotated[str|None, Header()]=None):
    if q!="secret-encrypted-token":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token!")
    
async def verify_key(q:Annotated[str|None, Header()]=None):
    if q!="secret-encoded-key":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Key!")
    return {"q":q}

app=FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])

@app.get("/items/")
async def get_item():
    return [{"name":"Yellow"},{"place":"The Piano Hub"},{"Food":"Pizza"}]

@app.get("/cars/")
async def get_car():
    return [{"Brand":"Mercedes"},{"Type":"GLE"},{"Price":10000000}]