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

class Offer(BaseModel):
    name:str
    description:str|None=None
    price:float
    items:list[Item]

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

# Bodies of pure lists¶
# If the top level value of the JSON body you expect is a JSON array (a Python list), you can declare the type in the parameter of the function, the same as in Pydantic models:
class Image2(BaseModel):
    url:HttpUrl
    name:str

@app.post("/images/multiple")
async def post_multiple_images(images:list[Image2]):
    return images

#Example body:
[
  {
    "url": "https://example.com/cat.png",
    "name": "Cute Cat"
  },
  {
    "url": "https://example.com/dog.png",
    "name": "Happy Dog"
  },
  {
    "url": "https://example.com/bird.png",
    "name": "Flying Bird"
  }
]

# Bodies of arbitrary dicts
@app.post("/weights/")
async def post_weight(weights:dict[int, float]):
    return weights
