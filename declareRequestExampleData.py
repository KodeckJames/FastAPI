from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated

app=FastAPI()

# Extra JSON Schema data in Pydantic models¶
class Item(BaseModel):
    name:str=Field(examples=["Foo"])
    description:str|None=Field(default=None, examples=["This is the best FastAPI course"])
    price:float=Field(examples=[9.99])
    tax:float|None=Field(default=None, examples=[0.78])

    model_config={
        "json_schema_extra":{
            "examples":[
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }

@app.put("/items/{item_id}")
async def put_item(item_id:int, item:Annotated[Item, Body(openapi_examples={
     "normal": {
        "summary": "A normal example",
        "description": "A **normal** item works correctly.",
        "value": {
            "name": "Foo",
            "description": "A very nice Item",
            "price": 35.4,
            "tax": 3.2,
        },
    },
    "converted": {
        "summary": "An example with converted data",
        "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
        "value": {
            "name": "Bar",
            "price": "35.4",
        },
    },
    "invalid": {
        "summary": "Invalid data is rejected with an error",
        "value": {
            "name": "Baz",
            "price": "thirty five point four",
        },
                },
} ,examples=[{
        "name": "Foo",
        "description": "A very nice Item",
        "price": 35.4,
        "tax": 3.2,
    },
    {
        "name": "Bar",
        "price": "35.4",
    },
    {
        "name": "Baz",
        "price": "thirty five point four",
    },])]):
    result={"item_id":item_id, "item":item}
    return result