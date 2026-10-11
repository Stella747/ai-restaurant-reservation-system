from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routes import reservations, tables, guests

app = FastAPI(
    title="Restaurant Reservation API",
    description="AI-assisted reservations for The Gourmet Grill (AWS Gen AI Hackathon)",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(reservations.router, prefix="/api")
app.include_router(tables.router, prefix="/api")
app.include_router(guests.router, prefix="/api")


@app.get("/health")
def health_check():
    return {"status": "ok"}