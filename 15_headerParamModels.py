from fastapi import FastAPI, Header
from pydantic import BaseModel
from typing import Annotated

app=FastAPI()

class CommonHeaders(BaseModel):
    model_config={"extra":"forbid"}

    host:str
    save_data:bool
    if_modified_since:str|None=None
    traceparent:str|None=None
    x_tag:list[str]=[]
    
@app.get("/items/")
async def get_items(headers:Annotated[CommonHeaders, Header(convert_underscores=True)]):
    return headers
