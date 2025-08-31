import re
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="MrCookies API", version="1.0")

# Lista que simula base de datos
usuarios = []

# Modelo de datos para recibir por JSON
class Registro(BaseModel):
    nombre: str = Field(..., min_length=1, description="Nombre del usuario")
    telefono: str = Field(..., min_length=1, description="Número de teléfono")
    correo: str = Field(..., min_length=5, description="Correo electrónico")

@app.post("/registro")
def post_registro(data: Registro):
    # Validar nombre
    if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$", data.nombre):
        raise HTTPException(status_code=400, detail="El nombre solo debe contener letras.")

    # Validar teléfono
    if not re.match(r"^[0-9]+$", data.telefono):
        raise HTTPException(status_code=400, detail="El teléfono solo debe contener números.")

    # Validar correo
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", data.correo):
        raise HTTPException(status_code=400, detail="Ingresa un correo electrónico válido.")

    # Verificar que no esté registrado ya
    if any(u['correo'] == data.correo for u in usuarios):
        raise HTTPException(status_code=400, detail="Este correo ya está registrado.")

    # Guardar usuario
    usuarios.append({
        "nombre": data.nombre,
        "telefono": data.telefono,
        "correo": data.correo
    })

    return {"status": "ok", "mensaje": f"Usuario '{data.nombre}' registrado correctamente."}

@app.get("/usuarios")
def get_usuarios():
    return {"usuarios": usuarios}
