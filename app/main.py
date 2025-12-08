from fastapi import FastAPI
from app.routes.export_router import router as export_router
from app.routes import clientes_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Python CSV Service running"}

app.include_router(export_router, prefix="/api/clientes", tags=["Clientes"])

app.include_router(clientes_router.router, prefix="/api/clientes", tags=["Clientes"])
