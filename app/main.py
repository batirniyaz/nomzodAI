import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.auth.auth_backend import router as auth_router
from app import router

from app.auth.database import create_db_and_tables


@asynccontextmanager
async def lifespan(main_app: FastAPI):
    await create_db_and_tables()

    yield

app = FastAPI(
    title="NomzodAI",
    version="0.1",
    summary="Program that will take interview by itself with AI.",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"message": "Hello, This is root path NomzodAI!"}

app.include_router(auth_router)
app.include_router(router)
app.mount("/storage", StaticFiles(directory="app/storage"), name="storage")
