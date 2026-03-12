from fastapi import FastAPI
from app.routers import health # health endpoint

app = FastAPI(title="Farkle API", version = "0.1.0")

app.include_router(health.router, prefix="/health", tags=["health"])