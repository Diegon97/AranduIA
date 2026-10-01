"""
Rutas API para el Módulo Docente / Copiloto del Aula.
"""

from fastapi import APIRouter, HTTPException
from src.core.teacher_copilot import (
    TeacherCopilot,
    PlanLeccionRequest,
    PlanLeccionResponse,
    RubricaRequest,
    RubricaResponse,
)

router = APIRouter(prefix="/api/docente", tags=["Copiloto Docente"])
copilot = TeacherCopilot()


@router.post("/planificar", response_model=PlanLeccionResponse)
async def planificar_clase(req: PlanLeccionRequest):
    """Genera un plan de clase completo con momentos didácticos según el MEC."""
    if not req.tema.strip():
        raise HTTPException(status_code=400, detail="El tema no puede estar vacío.")
    return await copilot.generar_plan(req)


@router.post("/rubrica", response_model=RubricaResponse)
async def generar_rubrica(req: RubricaRequest):
    """Genera una rúbrica analítica por niveles de desempeño."""
    if not req.tema.strip():
        raise HTTPException(status_code=400, detail="El tema no puede estar vacío.")
    return await copilot.generar_rubrica(req)
