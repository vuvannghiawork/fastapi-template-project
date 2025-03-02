from fastapi import APIRouter


hello_router = APIRouter(prefix="/hello", tags=["hello"])


@hello_router.post("/login")
async def login():
    return {"message": "Login successful"}


@hello_router.get("/xxxxxxxxxx")
def root():
    return {"message": "Hello index_router"}
