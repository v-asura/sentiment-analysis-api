from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from sentiment_analysis_api.api.routes import router
from sentiment_analysis_api.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting Sentiment Analysis API...")
    yield
    print("Shutting down Sentiment Analysis API...")


app = FastAPI(
    title="Sentiment Analysis API",
    description="A microservice for text sentiment analysis",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(
        "sentiment_analysis_api.main:app",
        host="0.0.0.0",
        port=settings.PORT,
        reload=settings.DEBUG,
    )
