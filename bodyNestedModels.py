from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app=FastAPI()

class Image(BaseModel):
    url:HttpUrl
    name:str

class Item(BaseModel):
    name:str
    description:str|None=None
    price:float
    tax:float|None=None
    prizes:list[str]=[]
    tags:set[str]=()
    image:Image|None=None
    photos:list[Image]|None=None

@app.put("/item/{item_id}")
async def put_item(item_id:int, item:Item):
    result={"item_id":item_id, "item":item}
    return result

# This would mean that FastAPI would expect a body similar to:
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": ["rock", "metal", "bar"],
    "image": {
        "url": "http://example.com/baz.jpg",
        "name": "The Foo live"
    }
}

# You can also use Pydantic models as subtypes of list, set, etc. as in line 18
# This will expect (convert, validate, document, etc.) a JSON body like
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": [
        "rock",
        "metal",
        "bar"
    ],
    "images": [
        {
            "url": "http://example.com/baz.jpg",
            "name": "The Foo live"
        },
        {
            "url": "http://example.com/dave.jpg",
            "name": "The Baz"
        }
    ]
}