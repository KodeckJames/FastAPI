from fastapi import FastAPI, Depends, Cookie, Query
from typing import Annotated

app=FastAPI()

def get_query(q:Annotated[str|None, Query()]=None):
    return {"q":q}

def get_query_or_cookie(q:Annotated[str, Depends(get_query)], cookie:Annotated[str|None, Cookie()]=None):
    if not q:
        return{"cookie":cookie}
    return {"q":q}

@app.get("/items/")
async def get_item(queryOrCookie:Annotated[get_query_or_cookie, Depends()]):
# async def get_item(queryOrCookie:Annotated[str, Depends(get_query_or_cookie)]): -> Also works
    return queryOrCookie

# USING THE SAME DEPENDENCY MULTIPLE TIMES
# If one of your dependencies is declared multiple times for the same path operation, for example, multiple dependencies have a common sub-dependency, FastAPI will know to call that sub-dependency only once per request.

# And it will save the returned value in a "cache" and pass it to all the "dependants" that need it in that specific request, instead of calling the dependency multiple times for the same request.

# NB:- cache is a utility/ system used to store generated values and reuse them instead of computing them again

# In an advanced scenario where you know you need the dependency to be called at every step (possibly multiple times) in the same request instead of using the "cached" value, you can set the parameter use_cache=False when using Depends:
async def needy_dependency(fresh_value: Annotated[str, Depends(get_query, use_cache=False)]):
    return {"fresh_value": fresh_value}