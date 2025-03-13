from fastapi import FastAPI
from src.api.v1.endpoints.arch_bytes_generator import router as arch_bytes_router
from src.core.logging import settings

app = FastAPI(title="Software Architecture Information Generator", version="0.1.0")
app.include_router(arch_bytes_router, prefix="/api/v1/")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Software Architecture Information Generator!"}