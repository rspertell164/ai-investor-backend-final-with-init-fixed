from fastapi import APIRouter, Request
import random

router = APIRouter()

@router.post("/predict")
async def predict(request: Request):
    data = await request.json()
    input_text = data.get("text", "")
    # Simulated analysis
    sentiments = ["positive", "neutral", "negative"]
    sentiment = random.choice(sentiments)
    confidence = round(random.uniform(0.7, 0.99), 2)
    return {
        "input": input_text,
        "sentiment": sentiment,
        "confidence": confidence,
        "message": f"The sentiment of your input is {sentiment} (confidence: {confidence})"
    }
