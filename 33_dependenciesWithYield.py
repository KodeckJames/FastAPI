# FastAPI supports dependencies that do some extra steps after finishing.
# Extra things is sometimes also called exit code, cleanup code, teardown code, closing code, context manager exit code, etc.

# For example, you could use this to create a database session and close it after finishing.

# Only the code prior to and including the yield statement is executed before creating a response:

# The yielded value is what is injected into path operations and other dependencies:
from fastapi import Depends
from typing import Annotated

def DBSession():
    pass

async def get_db():
    db=DBSession()
    try:
        yield db
    finally:
        db.close()

# The code following the yield statement is executed after the response:

# Sub-dependencies with yield
def generate_dep_a():
    pass
def generate_dep_b():
    pass
def generate_dep_c():
    pass

async def dependency_a():
    dep_a=generate_dep_a()
    try:
        yield dep_a
    finally:
        dep_a.close()

async def dependency_b(dep_a:Annotated[str, Depends(dependency_a)]):
    dep_b=generate_dep_b()
    try:
        yield dep_b
    finally:
        dep_b.close(dep_a)

async def dependency_c(dep_b:Annotated[str, Depends(dependency_b)]):
    dep_c=generate_dep_c()
    try:
        yield dependency_c
    finally:
        dep_c.close(dep_b)



    