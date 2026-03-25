# main_api.py
from fastapi import FastAPI
import uvicorn
from app.api.routers.users import router as users_router

app = FastAPI(
    title="Gym Bot API",
    description="API для фитнес бота",
    version="0.1.0"
)

app.include_router(users_router)

@app.get("/")
async def root():
    return {
        "message": "Gym Bot API",
        "status": "running"
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("main_api:app", host="0.0.0.0", port=8000, reload=True)