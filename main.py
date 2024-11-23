from routers import offers

from fastapi import FastAPI
from dotenv import load_dotenv
import pathlib
from fastapi.middleware.cors import CORSMiddleware
import firebase_admin
from config import get_settings

app = FastAPI()
routers = [
    # (auth.router, "/auth", ["auth"]),
    offers.router,
    # (filters.router, "/filters", ["filters"]),
]
[app.include_router(router) for router in routers]

settings = get_settings()
basedir = pathlib.Path(__file__).parents[1]
load_dotenv(basedir /"BE/.env")

firebase_admin.initialize_app()

origins = [settings.frontend_url]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





