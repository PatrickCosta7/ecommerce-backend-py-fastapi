from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import text
from app.api.api import api_router
from app.db.session import engine
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Attempting to connect to DB")

    async with engine.begin() as conn:
        await conn.execute(text("SELECT 1"))

    print("Successfully connected to DB")

app = FastAPI(title="ShopeEase API", version="0.1.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins =["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api_router, prefix="/api")
