from fastapi import FastAPI

app=FastAPI()

#FastAPI allows you to declare additional information and validation for your parameters.
@app.get("/items/")
async def get_item(q:str|None=None):
    item_list={"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        item_list.update({"q":q})
    return item_list