from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.models.user import User
from app.models.url import URL

from app.routes import auth_routes, url_routes

app = FastAPI(title="Mini URL Shortener API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


app.include_router(auth_routes.router)
app.include_router(url_routes.router)


@app.get("/")
def home():
    return {"message": "API running"}