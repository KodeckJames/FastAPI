from fastapi import FastAPI, HTTPException, Path
from typing import Annotated

app=FastAPI()

items={
    "car":"This is a Mercedes SUV called the GLE"
}

@app.get("/items/{item_id}")
async def get_item(item_id:Annotated[str, Path()]):
    if item_id not in items:
        raise HTTPException(detail={"Error":"This item doesn't exist"}, status_code=404)
    return items[item_id]