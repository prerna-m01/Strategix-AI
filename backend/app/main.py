from fastapi import FastAPI

app = FastAPI(
    title="Strategix AI",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Strategix AI 🚀"
    }