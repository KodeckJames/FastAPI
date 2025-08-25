from fastapi import FastAPI, Query
from typing import Annotated

app=FastAPI()

#FastAPI allows you to declare additional information and validation for your parameters.
@app.get("/items/")
async def get_item(q:str|None=None):
    item_list={"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        item_list.update({"q":q})
    return item_list

#Additional validation
#We are going to enforce that even though q is optional, whenever it is provided, its length doesn't exceed 50 characters.
#Annotated comes from Python’s typing module.
#It’s a way to attach extra metadata (like validation rules, descriptions, or docs info) to a type.
#Syntax:
#Annotated[<base type>, <extra metadata>]

@app.get("/itemz/")
async def read_item(q: Annotated[str|None, Query(max_length=50)]=None):
    results={"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results

#Use Annotated in the type for the q parameter

#Adding more validations
@app.get("/itemx/")
async def get_item(q:Annotated[str|None, Query(max_length=20, min_length=3)]=None):
    results={"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results

#Adding regular expressions
@app.get("/itemsis/")
async def get_item(q:Annotated[str|None, Query(max_length=20, min_length=3, pattern="^fixedquery$")]=None):
    results={"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results

#Default values
@app.get("/itemdef/")
async def get_item(q:Annotated[str|None, Query(min_length=3, max_length=20)]="fixedQuery"):
    results={"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results