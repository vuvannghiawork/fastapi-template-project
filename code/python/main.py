import settings
from loguru import logger
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from index_router import index_router


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(index_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Hello World"}


if __name__ == "__main__":

    logger.info(f"Starting application with FASTAPI_ENVIRONMENT={settings.FASTAPI_ENVIRONMENT}")

    if settings.FASTAPI_ENVIRONMENT == "DEVELOPMENT":
        uvicorn.run("main:app", host=settings.SERVER_IP, port=settings.SERVER_PORT, reload=True)
    else:
        uvicorn.run("main:app", host=settings.SERVER_IP, port=settings.SERVER_PORT)
