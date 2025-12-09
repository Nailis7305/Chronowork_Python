from fastapi import FastAPI
from app.routes.export_router import router as export_router
from app.routes.clientes_router import router as clientes_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Python CSV Service running"}

# Rutas de exportación
app.include_router(export_router, prefix="/api/export", tags=["Exportación"])

# Rutas de clientes
app.include_router(clientes_router, prefix="/api/clientes", tags=["Clientes"])

