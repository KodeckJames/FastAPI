# Creating a dependency/ dependable
# A dependency is just a function that can take all the parameters that a path operation function can take
from fastapi import FastAPI, Depends
from typing import Annotated

app=FastAPI()

async def common_params(q:str|None=None, skip:int=0, limit:int=100):
    return{"q":q, "skip":skip, "limit":limit}

type CommonDeps=Annotated[dict, Depends(common_params)]

@app.get("/items")
async def get_items(commons:Annotated[dict, Depends(common_params)]):
    return commons

@app.get("/users")
async def get_users(user_commons:Annotated[dict, Depends(common_params)]):
    return user_commons

# Alternative to prevent duplication by sharing Annotated dependencies
@app.get("/objects")
async def get_objects(commons:CommonDeps):
    return commons