from fastapi import FastAPI
from app.routes.export_router import router as export_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Python CSV Service running"}

app.include_router(export_router, prefix="/api/clientes", tags=["Clientes"])

