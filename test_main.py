
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_agregar_listar_videojuego():
    resp = client.post("/videojuegos", json={"id": 1, "nombre": "Zelda", "genero": "Aventura", "precio": 60})
    assert resp.status_code == 200

    resp = client.get("/videojuegos")
    assert resp.status_code == 200
    assert len(resp.json()) == 1

def test_aplicar_descuento():
    resp = client.put("/videojuegos/1/descuento?descuento=20")
    assert resp.status_code == 200
    assert resp.json()["nuevo_precio"] == 48.0
