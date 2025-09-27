from fastapi import FastAPI, Body, Path
from typing import Annotated
from datetime import datetime, time, timedelta
from uuid import UUID

app=FastAPI()

@app.put("/items/{item_id}")
async def put_items(
    item_id:Annotated[UUID, Path()],
    start_date:Annotated[datetime, Body()],
    end_date:Annotated[datetime, Body()],
    process_after:Annotated[timedelta, Body()],
    repeat_at:Annotated[time|None, Body()]=None    
):
    start_process=start_date+process_after
    duration=end_date-start_process
    return{
        "item_id":item_id,
        "start_datetime":start_date,
        "end_datetime":end_date,
        "process_after":process_after,
        "repeat_at":repeat_at,
        "start_process":start_process,
        "duration":duration
    }