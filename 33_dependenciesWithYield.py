# FastAPI supports dependencies that do some extra steps after finishing.
# Extra things is sometimes also called exit code, cleanup code, teardown code, closing code, context manager exit code, etc.

# For example, you could use this to create a database session and close it after finishing.

# Only the code prior to and including the yield statement is executed before creating a response:

# The yielded value is what is injected into path operations and other dependencies:

def DBSession():
    pass

async def get_db():
    db=DBSession()
    try:
        yield db
    finally:
        db.close()

# The code following the yield statement is executed after the response: