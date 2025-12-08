import csv
import os
from app.database import db

def generar_csv_clientes():
    coleccion = db["clientes"]
    datos = list(coleccion.find({}, {"_id": 0}))

    # Ruta segura en Render
    file_path = "/tmp/clientes_export.csv"

    header = datos[0].keys() if datos else []

    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(datos)

    return file_path
