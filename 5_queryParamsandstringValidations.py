from fastapi import FastAPI, Query
from typing import Annotated
import random
from pydantic import AfterValidator

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

@app.get("/addval/")
async def read_item(q: Annotated[str|None, Query(max_length=50)]=None):
    results={"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results

#Use Annotated in the type for the q parameter

#Adding more validations
@app.get("/moreval/")
async def get_item(q:Annotated[str|None, Query(max_length=20, min_length=3)]=None):
    results={"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results

#Adding regular expressions
@app.get("/regex/")
async def get_item(q:Annotated[str|None, Query(max_length=20, min_length=3, pattern="^fixedquery$")]=None):
    results={"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results

#Default values
@app.get("/defaults/")
async def get_item(q:Annotated[str|None, Query(min_length=3, max_length=20)]="fixedQuery"):
    results={"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results

#Required parameters
@app.get("/reqparams/")
async def get_item(q:Annotated[str|None, Query(max_length=20, min_length=3)]):
    results={"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results

#Query parameter list / multiple values
#For example, to declare a query parameter q that can appear multiple times in the URL, you can write:

@app.get("/multvalues/")
async def get_item(q:Annotated[list[str]|None, Query()]=None):
    query_items={"q":q}
    return query_items

#Query parameter list / multiple values with defaults
@app.get("/multvaluesdef/")
async def get_item(q:Annotated[list[str]|None, Query()]=["Bar", "Foo","yesyes","nono","maybe"]):
    query_items = {"q": q}
    return query_items

#Using just list
@app.get("/list/")
async def get_item(q:Annotated[list, Query()]):
    query_items = {"q": q}
    return query_items
#Keep in mind that in this case, FastAPI won't check the contents of the list.

#Declaring more Metadata
#That information will be included in the generated OpenAPI and used by the documentation user interfaces and external tools.
@app.get("/metadata/")
async def get_items(q:Annotated[str, Query(title="Query string", description="Query string for the items to search in the database that have a good match", min_length=3)]=None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#Alias parameters
@app.get("/alias/")
async def get_item(q:Annotated[str|None, Query(alias="item-query")]=None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#Deprecating Parameters
@app.get("/deprecated/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

#Excluding Parameters from OpenAPI
@app.get("/exclude/")
async def get_item(hidden_query:Annotated[str|None, Query(include_in_schema=False)]=None):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}
    
#Custom Validation
data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}

def check_valid_id(id: str):
    if not id.startswith(("isbn-","imdb")):
        raise ValueError("Invalid ID format, it must start with 'isbn-' or 'imdb-'")
    return id

@app.get("customvalidation")
async def get_item(id:Annotated[str|None, AfterValidator(check_valid_id)]=None):
    if id:
        item=data.get(id)
    else:
        id, item = random.choice(list(data.items()))
    return {"id":id, "name":item}