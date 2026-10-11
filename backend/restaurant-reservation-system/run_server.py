"""Start the FastAPI server (run from backend/restaurant-reservation-system)."""

import main  # noqa: F401 — ensures DynamoDB table exists

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "src.api.app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
