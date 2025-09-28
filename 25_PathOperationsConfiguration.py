from fastapi import FastAPI, status
from pydantic import BaseModel
from enum import Enum

app=FastAPI()

# Response Status Code
class Item(BaseModel):
    name:str
    message:str|None=None
    price:int
    tax:float|None=None
    tags:set[str]=set()

@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item:Item):
    return item

# Tags
# In FastAPI, the tags parameter inside a route decorator (like @app.post, @app.get, etc.) is not about your app’s logic — it’s mainly for documentation and organization purposes.
# Here’s what it does:
# Groups endpoints in the automatically generated API docs (Swagger UI and ReDoc).
# If you add tags=["items"], that endpoint will appear under the "items" section in the Swagger UI (/docs) and ReDoc (/redoc).
# This helps when you have many routes, so you can organize them logically (e.g., ["users"], ["auth"], ["orders"]).
# Does not affect functionality.
# It won’t change how your API works or how requests/responses are processed.
# It’s purely metadata for documentation.

@app.post("/tags/", response_model=Item, tags=["items"])
async def tag_item(item:Item):
    return item

@app.get("/gettags/", tags=["items"])
async def get_item():
    return [{"Name":"Foo", "Price":95}]

@app.get("/users/", tags=["users"])
async def get_user():
    return[{"name":"JJ"}]

# Tags with enums
class Tags(Enum):
    items="items"
    users="users"

@app.get("/itemsenum/", tags=[Tags.items])
async def get_items_enum():
    return ["Portal gun","Plumbus"]

@app.get("/usersenum/", tags=[Tags.users])
async def get_item_useenum():
    return["Rick", "Morty"]

# Description and summary
@app.post("/itemz/", response_model=Item, summary="Personal details", description="Add your details as required")
async def post_item_with_summary(item:Item):
    return item

# Description from docstring
@app.post("/docstringdescription/", summary="Just post something!")
async def post_item(item:Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item

# Response description
@app.post("/docstringresponsedescription/", summary="Just post something!", response_description="The created item")
async def post_item(item:Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item