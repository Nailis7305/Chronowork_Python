from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.services.export_service import generar_csv_clientes

router = APIRouter()

@router.get("/export")
async def exportar_clientes():
    file_path = generar_csv_clientes()
    return FileResponse(
        file_path,
        media_type="text/csv",
        filename="clientes.csv"
    )
