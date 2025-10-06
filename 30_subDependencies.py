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
