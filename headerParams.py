from fastapi import FastAPI, Header
from typing import Annotated

app=FastAPI()

@app.get("/items/")
async def get_items(header:Annotated[list[str]|None, Header(convert_underscores=False)]=None):
    result={"header":header}
    return result

#Duplicate headers
# It is possible to receive duplicate headers. That means, the same header with multiple values.
# If you communicate with that path operation sending two HTTP headers like:

# header: foo
# header: bar

# The response would be like:

# {
#     "header values": [
#         "bar",
#         "foo"
#     ]
# }