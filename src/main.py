from fastapi import FastAPI
from shared.infrasctructure.api import router as shared_router
from resources.infrastructure.api import router as resources_router

app = FastAPI()

app.include_router(shared_router)
app.include_router(resources_router)