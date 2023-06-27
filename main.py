from fastapi import FastAPI

from app.config import settings
from app.routes import router as text_entry_router
from logger import log

app = FastAPI(
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
    title="Netvision test task",
    version="0.1.0",
)
app.include_router(text_entry_router, prefix="/api/v1")


@app.get("/healthcheck", status_code=200)
async def healthcheck():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    log("start app")
    uvicorn.run(app, host=settings.APP_HOST, port=int(settings.APP_PORT))
