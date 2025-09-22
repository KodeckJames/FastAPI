from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app=FastAPI()

@app.get("/items/", status_code=201)
async def get_item(name:str):
    return {"name":name}