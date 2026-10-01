"""
Rutas API para sincronización Offline-First y estado del sistema.
"""

from fastapi import APIRouter
from src.config import settings
from src.core.jopara_engine import JoparaEngine
from src.core.socratic_tutor import SocraticTutor

router = APIRouter(prefix="/api/sync", tags=["Sincronización Offline"])


@router.get("/status")
async def estado_sistema():
    """Estado de salud, modo de inferencia y soporte offline."""
    return {
        "sistema": settings.APP_NAME,
        "entorno": settings.APP_ENV,
        "proveedor_ia": settings.LLM_PROVIDER,
        "offline_first": True,
        "ley_7593_activa": settings.ENFORCE_DATA_MINIMIZATION,
        "bilingue": True,
    }


@router.get("/offline-pack")
async def paquete_offline():
    """
    Retorna el paquete completo de recursos para almacenamiento local en PWA / IndexedDB.
    Permite operar 100% desconectado en aulas rurales.
    """
    return {
        "glosario_jopara": JoparaEngine.GLOSARIO,
        "frases_aliento": JoparaEngine.ALIENTOS,
        "pictogramas": SocraticTutor.PICTOGRAMAS_MAP,
        "materias_disponibles": [
            "Matemática",
            "Lengua y Literatura Castellana",
            "Lengua Guaraní",
            "Ciencias de la Naturaleza y de la Salud",
            "Ciencias Sociales",
        ],
        "grados_soportados": [
            "Educación Inicial (4 a 5 años)",
            "1° Ciclo EEB (1° a 3° grado)",
            "2° Ciclo EEB (4° a 6° grado)",
            "3° Ciclo EEB (7° a 9° grado)",
            "Bachillerato Científico y Técnico (1° a 3° curso)",
        ],
    }
