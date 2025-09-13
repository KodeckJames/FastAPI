from fastapi import FastAPI, Cookie
from typing import Annotated

app=FastAPI()

@app.get("/items/")
async def get_item(ads_id:Annotated[str | None, Cookie(alias="cookie")]=None):
    result={"ads_id":ads_id}
    return result
