import pytest
from src.core.socratic_tutor import SocraticTutor, TutorRequest


@pytest.mark.asyncio
async def test_socratic_tutor_math_guidance():
    tutor = SocraticTutor()
    req = TutorRequest(
        mensaje="¿Cuánto es 8 por 7?",
        materia="matematica",
        modo_tea=False
    )
    res = await tutor.responder(req)
    assert res.es_socratica is True
    # El tutor no debe dar simplemente "56"
    assert "56" not in res.respuesta
    assert "?" in res.respuesta  # Debe terminar o contener pregunta guía


@pytest.mark.asyncio
async def test_socratic_tutor_tea_mode():
    tutor = SocraticTutor()
    req = TutorRequest(
        mensaje="sumar números",
        materia="matematica",
        modo_tea=True
    )
    res = await tutor.responder(req)
    assert res.modo_tea_activo is True
    assert "Paso 1:" in res.respuesta
    assert len(res.pictogramas) > 0
    conceptos = [p["concepto"] for p in res.pictogramas]
    assert "sumar" in conceptos


@pytest.mark.asyncio
async def test_socratic_tutor_jopara_detection():
    tutor = SocraticTutor()
    req = TutorRequest(
        mensaje="Mba'éichapa che mbo'ehara, ikatu chepytyvõ?",
        materia="general",
        idioma_preferido="jopara"
    )
    res = await tutor.responder(req)
    assert res.aliento_jopara is not None
