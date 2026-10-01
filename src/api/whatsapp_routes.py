"""
Rutas API para el Gateway de WhatsApp (docentes y zonas de conectividad móvil limitada).
"""

from fastapi import APIRouter, Query, Response, status
from pydantic import BaseModel
from typing import Dict, Any, Optional
from src.config import settings
from src.core.teacher_copilot import TeacherCopilot, PlanLeccionRequest
from src.core.socratic_tutor import SocraticTutor, TutorRequest

router = APIRouter(prefix="/api/whatsapp", tags=["WhatsApp Gateway"])
copilot = TeacherCopilot()
tutor = SocraticTutor()


class SimulateMessageRequest(BaseModel):
    remitente_tipo: str = "docente"  # "docente" o "estudiante"
    texto: str


@router.get("/webhook")
async def verificar_webhook(
    hub_mode: Optional[str] = Query(None, alias="hub.mode"),
    hub_verify_token: Optional[str] = Query(None, alias="hub.verify_token"),
    hub_challenge: Optional[str] = Query(None, alias="hub.challenge"),
):
    """Verificación de Webhook para Meta Cloud API."""
    if hub_mode == "subscribe" and hub_verify_token == settings.WHATSAPP_VERIFY_TOKEN:
        return Response(content=hub_challenge, media_type="text/plain")
    return Response(content="Verificación fallida", status_code=status.HTTP_403_FORBIDDEN)


@router.post("/simulate")
async def simular_mensaje_whatsapp(req: SimulateMessageRequest) -> Dict[str, Any]:
    """
    Endpoint para pruebas comunitarias y simulación de mensajes de WhatsApp
    sin requerir credenciales activas de Meta.
    """
    texto = req.texto.strip()
    if req.remitente_tipo == "docente":
        # Flujo Rumi-style para docentes
        plan = await copilot.generar_plan(
            PlanLeccionRequest(
                tema=texto,
                materia="General",
                grado_o_curso="EEB",
                incluir_adaptacion_tea=True,
            )
        )
        respuesta_whatsapp = (
            f"📋 *PLAN RÁPIDO ARANDUIA*\n"
            f"📚 *Tema:* {plan.tema}\n"
            f"🎯 *Capacidad:* {plan.capacidad_mec}\n\n"
            f"▶️ *Inicio (15 min):*\n{plan.inicio}\n\n"
            f"⚙️ *Desarrollo (50 min):*\n{plan.desarrollo}\n\n"
            f"🏁 *Cierre (15 min):*\n{plan.cierre}\n\n"
            f"🧩 *Adaptación TEA:* {plan.adaptacion_tea.get('instrucciones', 'N/A') if plan.adaptacion_tea else 'N/A'}"
        )
        return {"canal": "whatsapp", "destinatario": "docente", "mensaje_saliente": respuesta_whatsapp}

    # Flujo para estudiante
    tutor_res = await tutor.responder(TutorRequest(mensaje=texto, modo_tea=False))
    return {
        "canal": "whatsapp",
        "destinatario": "estudiante",
        "mensaje_saliente": f"💡 *AranduIA Tutor:* {tutor_res.respuesta}",
    }
