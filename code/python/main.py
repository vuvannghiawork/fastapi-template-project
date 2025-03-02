from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Xin chào! Đây là ứng dụng FastAPI chạy trên Docker"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}