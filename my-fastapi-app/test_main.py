import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_endpoint_assincrono():
    response = client.get("/endpoint_assincrono")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Este é um endpoint assíncrono"}

def test_endpoint_sincrono():
    response = client.get("/endpoint_sincrono")
    assert response.status_code == 200
    assert response.json() == {"mensagem": "Este é um endpoint síncrono"}

def test_endpoint_invalido():
    response = client.get("/endpoint_invalido")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
    