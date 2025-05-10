from fastapi import FastAPI

app = FastAPI(
    title="API Example",
    description="Shop API",
    version="0.1.0",
)

@app.get("/")
async def root() -> dict:
    return {"message": "Welcome to Shop API!"}
