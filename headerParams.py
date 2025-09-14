from fastapi import FastAPI, Header
from typing import Annotated

app=FastAPI()

@app.get("/items/")
async def get_items(header:Annotated[str, Header(convert_underscores=False)]):
    result={"header":header}
    return result
