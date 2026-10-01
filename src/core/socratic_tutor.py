"""
Motor del Tutor Socrático Adaptativo — AranduIA.
Enseña mediante preguntas guiadas, evita respuestas directas, incluye modo TEA y pictogramas.
"""

from typing import Dict, List, Optional
from pydantic import BaseModel
from src.core.llm_provider import BaseLLMProvider, LLMMessage, get_llm_provider
from src.core.security import DataMinimizer
from src.core.jopara_engine import JoparaEngine


class TutorRequest(BaseModel):
    mensaje: str
    materia: str = "general"  # "matematica", "lectura", "ciencias", "historia"
    modo_tea: bool = False
    modo_pictogramas: bool = False
    idioma_preferido: str = "es"  # "es", "gn" (guaraní), "jopara"
    historial: List[Dict[str, str]] = []


class TutorResponse(BaseModel):
    respuesta: str
    es_socratica: bool
    modo_tea_activo: bool
    pictogramas: List[Dict[str, str]]
    aliento_jopara: Optional[str]
    pistas_sugeridas: List[str]


class SocraticTutor:
    """Implementa la lógica del tutor socrático inclusivo."""

    PICTOGRAMAS_MAP: Dict[str, Dict[str, str]] = {
        "sumar": {"emoji": "➕", "etiqueta": "Sumar / Agregar"},
        "restar": {"emoji": "➖", "etiqueta": "Restar / Quitar"},
        "multiplicar": {"emoji": "✖️", "etiqueta": "Multiplicar"},
        "dividir": {"emoji": "➗", "etiqueta": "Dividir / Repartir"},
        "leer": {"emoji": "📖", "etiqueta": "Leer / Moñe'ẽ"},
        "escribir": {"emoji": "✍️", "etiqueta": "Escribir / Hai"},
        "pensar": {"emoji": "💡", "etiqueta": "Pensar / Idea"},
        "pregunta": {"emoji": "❓", "etiqueta": "Pregunta / Porandu"},
        "atencion": {"emoji": "👀", "etiqueta": "Observar"},
        "pausa": {"emoji": "⏳", "etiqueta": "Tomar un respiro"},
        "agua": {"emoji": "💧", "etiqueta": "Tomar agua / Tereré"},
        "bien": {"emoji": "⭐", "etiqueta": "¡Muy bien! / Iporã"},
    }

    def __init__(self, provider: Optional[BaseLLMProvider] = None):
        self.provider = provider or get_llm_provider()

    def _extraer_pictogramas(self, texto: str) -> List[Dict[str, str]]:
        """Identifica pictogramas pertinentes para el texto según conceptos clave."""
        palabras = texto.lower().split()
        encontrados = []
        for clave, picto in self.PICTOGRAMAS_MAP.items():
            if any(clave in p for p in palabras):
                encontrados.append({"concepto": clave, **picto})
        return encontrados

    def _construir_prompt_sistema(self, req: TutorRequest) -> str:
        """Construye las directivas estrictas para el LLM."""
        base = (
            "Sos AranduIA, un tutor socrático inteligente y paciente para estudiantes paraguayos de 4 a 18 años.\n"
            "REGLA DE ORO INQUEBRANTABLE: NUNCA des la respuesta directa o final a una tarea, ejercicio o pregunta del alumno.\n"
            "Tu misión es guiarlo mediante una sola pregunta reflexiva a la vez, usando analogías cotidianas de Paraguay.\n"
        )

        if req.modo_tea:
            base += (
                "\nMODO TEA / NEURODIVERGENTE ACTIVADO:\n"
                "- Usá oraciones cortas, lenguaje literal, directo y sin metáforas ambiguas ni ironías.\n"
                "- Dividí cualquier explicación en pasos numerados concretos (1, 2, 3).\n"
                "- Mantené un tono calmo, predecible y sin expresiones de urgencia.\n"
            )

        if req.idioma_preferido in ("gn", "jopara") or JoparaEngine.detectar_jopara(req.mensaje):
            base += (
                "\nMODO LINGÜÍSTICO JOPARA:\n"
                "- El estudiante se comunica en Guaraní o Jopara. Respondé en un Jopara natural, cálido y comprensible.\n"
                "- Validá sus expresiones culturales y pedagógicas.\n"
            )

        return base

    async def responder(self, req: TutorRequest) -> TutorResponse:
        """Procesa la interacción del estudiante y genera la guía socrática."""
        # Sanitizar entrada bajo Ley N° 7593/2025
        mensaje_limpio = DataMinimizer.sanitize_text(req.mensaje)

        # Construir mensajes
        messages = [LLMMessage(role="system", content=self._construir_prompt_sistema(req))]

        for turno in req.historial[-4:]:  # Últimos 2 turnos para contexto ligero
            role = "user" if turno.get("rol") == "usuario" else "assistant"
            messages.append(LLMMessage(role=role, content=turno.get("texto", "")))

        messages.append(LLMMessage(role="user", content=mensaje_limpio))

        # Inferir respuesta
        llm_res = await self.provider.generate_response(messages, temperature=0.3)

        # Enriquecimiento y procesamiento de reglas
        texto_salida = llm_res.content

        # Si el motor es local_rules, generamos una respuesta socrática estructurada según la materia
        if llm_res.provider == "local_rules":
            texto_salida = self._generar_respuesta_local(mensaje_limpio, req)

        pictogramas = self._extraer_pictogramas(mensaje_limpio + " " + texto_salida)
        aliento = JoparaEngine.frase_aliento() if (req.idioma_preferido in ("gn", "jopara") or JoparaEngine.detectar_jopara(mensaje_limpio)) else None

        # Sugerencias de pistas interactivas
        pistas = self._generar_pistas_sugeridas(req.materia, req.modo_tea)

        return TutorResponse(
            respuesta=texto_salida,
            es_socratica=True,
            modo_tea_activo=req.modo_tea,
            pictogramas=pictogramas,
            aliento_jopara=aliento,
            pistas_sugeridas=pistas,
        )

    def _generar_respuesta_local(self, mensaje: str, req: TutorRequest) -> str:
        """Generador socrático offline por heurística pedagógica."""
        m_lower = mensaje.lower()

        # Preguntas matemáticas
        if any(op in m_lower for op in ["cuanto es", "sumar", "+", "multiplicar", "x", "*", "dividir", "/"]):
            if req.modo_tea:
                return (
                    "Paso 1: Miremos los dos números que querés calcular.\n"
                    "Paso 2: ¿Podrías decirme qué operación te pide hacer el ejercicio? (¿Juntar o repartir?)"
                )
            return (
                "¡Excelente desafío! Para llegar a la solución juntos: "
                "¿Qué operación matemática identificás primero y qué número es el punto de partida?"
            )

        # Tareas generales o preguntas conceptuales
        if req.modo_tea:
            return (
                "Paso 1: Leí con atención tu pregunta.\n"
                "Paso 2: Pensá en una palabra clave sobre este tema.\n"
                "¿Qué es lo primero que te viene a la mente?"
            )

        return (
            "Es una gran pregunta para investigar. Antes de darte pistas: "
            "¿Qué sabés hasta ahora sobre este tema y qué parte te genera más dudas?"
        )

    def _generar_pistas_sugeridas(self, materia: str, modo_tea: bool) -> List[str]:
        """Pistas de apoyo para que el estudiante no se quede bloqueado."""
        if modo_tea:
            return [
                "1. Leer despacio la consigna",
                "2. Buscar la palabra clave",
                "3. Tomar una pausa si me siento cansado",
            ]
        return [
            "¿Podrías darme un ejemplo de tu vida cotidiana?",
            "¿Cuál sería el primer paso para resolverlo?",
            "¿Querés que lo dividamos en partes más sencillas?",
        ]
