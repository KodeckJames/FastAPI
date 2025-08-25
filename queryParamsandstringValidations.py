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

#Required parameters
@app.get("/itemreq/")
async def get_item(q:Annotated[str|None, Query(max_length=20, min_length=3)]):
    results={"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results

#Query parameter list / multiple values
#For example, to declare a query parameter q that can appear multiple times in the URL, you can write:

@app.get("/itemmult/")
async def get_item(q:Annotated[list[str]|None, Query()]=None):
    query_items={"q":q}
    return query_items

#Query parameter list / multiple values with defaults
@app.get("/itemmultdef/")
async def get_item(q:Annotated[list[str]|None, Query()]=["Bar", "Foo","yesyes","nono","maybe"]):
    query_items = {"q": q}
    return query_items

#Using just list
@app.get("/itemlistonly/")
async def get_item(q:Annotated[list, Query()]):
    query_items = {"q": q}
    return query_items
#Keep in mind that in this case, FastAPI won't check the contents of the list.

#Declaring more Metadata
#That information will be included in the generated OpenAPI and used by the documentation user interfaces and external tools.
@app.get("/itemstitle/")
async def get_items(q:Annotated[str, Query(title="Query string", description="Query string for the items to search in the database that have a good match", min_length=3)]=None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results