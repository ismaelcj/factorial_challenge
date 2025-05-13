from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.core.infrastructure.api.stockable_product.stockable_product_routes \
    import router as stockable_product_router
from backend.shared.infrastructure.dependencies import initial_setup


@asynccontextmanager
async def lifespan(app: FastAPI):
    initial_setup()
    yield

app = FastAPI(
    title="API Example",
    description="Shop API",
    version="0.1.0",
    lifespan=lifespan
)
app.include_router(stockable_product_router)

@app.get("/")
async def root() -> dict:
    return {"message": "Welcome to Shop API!"}
