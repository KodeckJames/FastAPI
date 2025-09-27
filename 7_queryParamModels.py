from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import Annotated, Literal

app=FastAPI()

class Model_defined(BaseModel):
    score:int=Field(100, gt=1, le=1000)
    marks:int=Field(20, gt=10)
    names:Literal['JJ','Ondix']="JJ"
    people:list[str]=[]

    #Forbid Extra Query Parameters
    model_config={"extra":"forbid"}

@app.get("/items/")
async def get_items(filtered:Annotated[Model_defined, Query()]):
    return filtered
