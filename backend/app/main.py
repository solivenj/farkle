from fastapi import FastAPI
from app.routers import health, turns

app = FastAPI(title="Farkle API", version = "0.1.0")

app.include_router(health.router)
app.include_router(turns.router)