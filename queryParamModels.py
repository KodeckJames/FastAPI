from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import Annotated, Literal

app=FastAPI()

class Model_defined(BaseModel):
    score:int=Field(100, gt=1, le=1000)
    marks:int=Field(0, gt=10)
    names:Literal['JJ','Ondix']="JJ"
    people:list[str]=[]

@app.get("/items/")
async def get_items(defined:Annotated[Model_defined, Query()]):
    return defined
