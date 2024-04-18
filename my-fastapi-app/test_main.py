import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from main import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_endpoint_assincrono():
    async with AsyncClient(app=app, base_url="http://endereco_base") as ac:
        response = await ac.get("/endpoint_assincrono")
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
    