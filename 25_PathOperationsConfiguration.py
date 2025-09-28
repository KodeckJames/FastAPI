from fastapi import FastAPI, status
from pydantic import BaseModel

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