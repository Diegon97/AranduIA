"""
Rutas API para el Módulo Estudiante / Tutor Socrático.
"""

from fastapi import APIRouter, HTTPException
from src.core.socratic_tutor import SocraticTutor, TutorRequest, TutorResponse
from src.core.jopara_engine import JoparaEngine

router = APIRouter(prefix="/api/tutor", tags=["Tutor Estudiante"])
tutor = SocraticTutor()


@router.post("/chat", response_model=TutorResponse)
async def chat_tutor(req: TutorRequest):
    """Procesa una consulta del estudiante y devuelve la orientación socrática."""
    if not req.mensaje.strip():
        raise HTTPException(status_code=400, detail="El mensaje no puede estar vacío.")
    return await tutor.responder(req)


@router.get("/pictogramas")
async def obtener_pictogramas():
    """Retorna el catálogo base de pictogramas educativos para modo accesible / TEA."""
    return {"pictogramas": SocraticTutor.PICTOGRAMAS_MAP}


@router.get("/glosario")
async def obtener_glosario():
    """Retorna términos pedagógicos en Guaraní Jopara."""
    return {"glosario": JoparaEngine.GLOSARIO}
