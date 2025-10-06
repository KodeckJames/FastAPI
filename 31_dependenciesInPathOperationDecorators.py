from fastapi import FastAPI, Depends, HTTPException, Header,status
from typing import Annotated

app=FastAPI()

async def verify_token(token:Annotated[str, Header()]):
    if token != "Fake-super-secret-token":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Token Header invalid")
    
async def verify_key(tokenKey:Annotated[str, Header()]):
    if tokenKey != "Fake-secret-super-key":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Token key is invalid")
    return tokenKey
    
@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def get_item():
    return [{"item": "Foo"}, {"item": "Bar"}]
