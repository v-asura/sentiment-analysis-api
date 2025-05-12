import pytest
from fastapi.testclient import TestClient

from sentiment_analysis_api.main import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_sentiment_positive():
    response = client.post("/api/v1/sentiment", json={"text": "I love this product!"})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "positive"


@pytest.mark.asyncio
async def test_sentiment_negative():
    response = client.post("/api/v1/sentiment", json={"text": "This is terrible!"})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "negative"


@pytest.mark.asyncio
async def test_sentiment_neutral():
    response = client.post("/api/v1/sentiment", json={"text": "This is a fact."})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "neutral"
