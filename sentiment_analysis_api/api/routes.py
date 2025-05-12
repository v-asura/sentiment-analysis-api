from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from sentiment_analysis_api.services.sentiment import analyze_sentiment

router = APIRouter()


class TextInput(BaseModel):
    text: str


@router.post("/sentiment", response_model=dict)
async def get_sentiment(input: TextInput):
    try:
        sentiment = analyze_sentiment(input.text)
        return {"text": input.text, "sentiment": sentiment}
    except Exception as e:
        raise HTTPException(  # noqa: B904
            status_code=500, detail=f"Error analyzing sentiment: {str(e)}"
        )  # noqa: B904
