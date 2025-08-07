from fastapi import FastAPI
from shared.infrasctructure.api import router as shared_router

app = FastAPI()

app.include_router(shared_router)