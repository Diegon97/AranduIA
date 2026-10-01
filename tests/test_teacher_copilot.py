import pytest
from src.core.teacher_copilot import TeacherCopilot, PlanLeccionRequest, RubricaRequest


@pytest.mark.asyncio
async def test_generar_plan_leccion_mec():
    copilot = TeacherCopilot()
    req = PlanLeccionRequest(
        tema="Fracciones Propias e Impropias",
        materia="Matemática",
        grado_o_curso="5° Grado EEB",
        incluir_adaptacion_tea=True
    )
    plan = await copilot.generar_plan(req)

    assert plan.tema == "Fracciones Propias e Impropias"
    assert "Matemática" in plan.capacidad_mec
    assert "Inicio" in plan.inicio
    assert "Desarrollo" in plan.desarrollo
    assert "Cierre" in plan.cierre
    assert len(plan.recursos) > 0
    assert "indicadores" in plan.evaluacion
    assert plan.adaptacion_tea is not None
    assert "apoyos_visuales" in plan.adaptacion_tea


@pytest.mark.asyncio
async def test_generar_rubrica():
    copilot = TeacherCopilot()
    req = RubricaRequest(
        tema="Comprensión de Textos Narrativos",
        materia="Lengua Castellana",
        grado="6° Grado"
    )
    rubrica = await copilot.generar_rubrica(req)
    assert len(rubrica.indicadores) == 3
    for ind in rubrica.indicadores:
        assert "criterio" in ind
        assert "logrado" in ind
        assert "en_proceso" in ind
        assert "no_logrado" in ind
