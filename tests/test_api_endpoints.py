import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_api_sync_status():
    res = client.get("/api/sync/status")
    assert res.status_code == 200
    data = res.json()
    assert data["sistema"] == "AranduIA"
    assert data["offline_first"] is True


def test_api_sync_offline_pack():
    res = client.get("/api/sync/offline-pack")
    assert res.status_code == 200
    data = res.json()
    assert "glosario_jopara" in data
    assert "pictogramas" in data


def test_api_tutor_pictogramas():
    res = client.get("/api/tutor/pictogramas")
    assert res.status_code == 200
    assert "sumar" in res.json()["pictogramas"]


def test_api_tutor_glosario():
    res = client.get("/api/tutor/glosario")
    assert res.status_code == 200
    assert "aprender" in res.json()["glosario"]


def test_api_tutor_chat():
    res = client.post("/api/tutor/chat", json={
        "mensaje": "Quiero aprender a sumar fracciones",
        "materia": "matematica",
        "modo_tea": True
    })
    assert res.status_code == 200
    data = res.json()
    assert data["es_socratica"] is True
    assert data["modo_tea_activo"] is True
    assert len(data["respuesta"]) > 0


def test_api_docente_planificar():
    res = client.post("/api/docente/planificar", json={
        "tema": "El Sistema Solar",
        "materia": "Ciencias de la Naturaleza",
        "grado_o_curso": "4° Grado",
        "incluir_adaptacion_tea": True
    })
    assert res.status_code == 200
    data = res.json()
    assert data["tema"] == "El Sistema Solar"
    assert "capacidad_mec" in data


def test_api_whatsapp_simulate():
    res = client.post("/api/whatsapp/simulate", json={
        "remitente_tipo": "docente",
        "texto": "Plan sobre la fotosíntesis"
    })
    assert res.status_code == 200
    data = res.json()
    assert data["canal"] == "whatsapp"
    assert "fotosíntesis" in data["mensaje_saliente"].lower()
