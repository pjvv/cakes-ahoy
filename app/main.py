from fastapi import FastAPI
from persistence.models import ensure_table_is_created
from views.v1.cakes import router as cakes_router

app = FastAPI(
    title="Cakes Ahoy!",
    description="CRUD API for tasty cakes",
    version="0.0.1",
)


###
# Register startup events
###
@app.on_event("startup")
def check_dynamodb():
    """Make sure the required table is created when the app starts."""
    ensure_table_is_created()


###
# Register routers
###
app.include_router(cakes_router, tags=["Cakes"])
