from fastapi import APIRouter
from pydantic import BaseModel
from app.database import db

router = APIRouter()

class Cliente(BaseModel):
    nombre: str
    email: str
    telefono: str
    direccion: str
    cedula: str

@router.post("/add")
def agregar_cliente(cliente: Cliente):
    coleccion = db["clientes"]
    coleccion.insert_one(cliente.dict())
    return {"message": "Cliente insertado correctamente"}
