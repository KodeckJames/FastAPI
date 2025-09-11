from fastapi import FastAPI
from pydantic import BaseModel, Field

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
async def put_item(item_id:int, item:Item):
    result={"item_id":item_id, "item":item}
    return result