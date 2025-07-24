from fastapi.testclient import TestClient
from main import app  # asumiendo que tu API está en main.py

client = TestClient(app)

def test_agregar_videojuego_exitoso():
    videojuego = {
        "id": 1,
        "nombre": "The Legend of Zelda",
        "genero": "Aventura",
        "precio": 50.0
    }
    response = client.post("/videojuegos", json=videojuego)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["nombre"] == "The Legend of Zelda"

def test_agregar_videojuego_duplicado():
    videojuego = {
        "id": 1,
        "nombre": "Super Mario Bros",
        "genero": "Plataformas",
        "precio": 40.0
    }
    # Ya existe el id 1 del test anterior
    response = client.post("/videojuegos", json=videojuego)
    assert response.status_code == 400
    assert response.json()["detail"] == "El videojuego ya existe"

def test_listar_videojuegos():
    response = client.get("/videojuegos")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1

def test_aplicar_descuento():
    response = client.put("/videojuegos/1/descuento?descuento=10")
    assert response.status_code == 200
    data = response.json()
    assert data["mensaje"] == "Descuento aplicado"
    assert "nuevo_precio" in data
    assert data["nuevo_precio"] == 45.0  # 50 - 10%

def test_eliminar_videojuego_exitoso():
    response = client.delete("/videojuegos/1")
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Videojuego eliminado"

def test_eliminar_videojuego_no_existente():
    response = client.delete("/videojuegos/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Videojuego no encontrado"
