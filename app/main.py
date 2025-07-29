from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import ai

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]  # Temporarily allow all for testing,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "Backend is running"}

# Include AI router
app.include_router(ai.router)
