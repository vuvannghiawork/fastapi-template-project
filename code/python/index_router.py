from fastapi import APIRouter


index_router = APIRouter()


@index_router.get("/xxxxxxxxxx")
def root():
    return {"message": "Hello index_router"}
