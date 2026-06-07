from fastapi import FastAPI

app = FastAPI(
    title="AI Career Coach API",
    version="1.0.0"
)


@app.get("/")
def health_check():
    return {
        "message": "AI Career Coach API is running"
    }