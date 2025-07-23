
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Videojuego(BaseModel):
    id: int
    nombre: str
    genero: str
    precio: float

videojuegos_db: List[Videojuego] = []

@app.get("/videojuegos", response_model=List[Videojuego])
def listar_videojuegos():
    return videojuegos_db

@app.post("/videojuegos", response_model=Videojuego)
def agregar_videojuego(videojuego: Videojuego):
    for v in videojuegos_db:
        if v.id == videojuego.id:
            raise HTTPException(status_code=400, detail="El videojuego ya existe")
    videojuegos_db.append(videojuego)
    return videojuego

@app.delete("/videojuegos/{videojuego_id}")
def eliminar_videojuego(videojuego_id: int):
    for v in videojuegos_db:
        if v.id == videojuego_id:
            videojuegos_db.remove(v)
            return {"mensaje": "Videojuego eliminado"}
    raise HTTPException(status_code=404, detail="Videojuego no encontrado")

@app.put("/videojuegos/{videojuego_id}/descuento")
def aplicar_descuento(videojuego_id: int, descuento: float):
    for v in videojuegos_db:
        if v.id == videojuego_id:
            v.precio *= (1 - descuento / 100)
            return {"mensaje": "Descuento aplicado", "nuevo_precio": v.precio}
    raise HTTPException(status_code=404, detail="Videojuego no encontrado")
