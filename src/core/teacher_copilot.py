"""
Módulo Copiloto Docente — AranduIA.
Automatiza la generación de planes de lección según normas del MEC,
rúbricas de evaluación y adaptaciones curriculares para TEA/Inclusión.
"""

from typing import Dict, List, Optional
from pydantic import BaseModel
from src.core.llm_provider import BaseLLMProvider, LLMMessage, get_llm_provider
from src.core.security import DataMinimizer


class PlanLeccionRequest(BaseModel):
    tema: str
    materia: str  # "Matemática", "Lengua Castellana", "Guaraní", "Ciencias", "Sociales"
    grado_o_curso: str  # Ej: "4° Grado EEB", "1° Curso Bachillerato"
    duracion_minutos: int = 80
    incluir_adaptacion_tea: bool = False
    idioma: str = "es"  # "es", "bilingue"


class PlanLeccionResponse(BaseModel):
    tema: str
    materia: str
    grado: str
    capacidad_mec: str
    inicio: str
    desarrollo: str
    cierre: str
    recursos: List[str]
    evaluacion: Dict[str, List[str]]
    adaptacion_tea: Optional[Dict[str, str]] = None


class RubricaRequest(BaseModel):
    tema: str
    materia: str
    grado: str


class RubricaResponse(BaseModel):
    tema: str
    indicadores: List[Dict[str, str]]


class TeacherCopilot:
    """Generador pedagógico asistido para docentes paraguayos."""

    def __init__(self, provider: Optional[BaseLLMProvider] = None):
        self.provider = provider or get_llm_provider()

    async def generar_plan(self, req: PlanLeccionRequest) -> PlanLeccionResponse:
        """Crea un plan de lección completo y estructurado bajo pautas curriculares del MEC."""
        tema_sanitizado = DataMinimizer.sanitize_text(req.tema)

        # Generación estructurada
        capacidad = (
            f"Aplica conceptos y destrezas fundamentales de {req.materia} "
            f"en la resolución de situaciones problemáticas referidas a {tema_sanitizado}."
        )

        inicio = (
            f"Momento de Inicio:\n"
            f"1. Saludo cordial y activación de conocimientos previos (15 min).\n"
            f"2. Pregunta detonante: ¿Dónde vemos o usamos '{tema_sanitizado}' en nuestra comunidad?\n"
            f"3. Presentación del objetivo de aprendizaje en pizarra en Español y Guaraní."
        )

        desarrollo = (
            f"Momento de Desarrollo:\n"
            f"1. Explicación dialogada y modelado de situaciones concretas (30 min).\n"
            f"2. Trabajo grupal colaborativo: resolución de guía de actividades prácticas (20 min).\n"
            f"3. Socialización guiada y puesta en común de estrategias empleadas por los estudiantes."
        )

        cierre = (
            f"Momento de Cierre:\n"
            f"1. Síntesis metacognitiva (15 min): ¿Qué aprendimos hoy y para qué nos sirve?\n"
            f"2. Verificación rápida de comprensión mediante tarjeta de salida o ejercicio breve.\n"
            f"3. Registro en cuaderno y despedida motivacional."
        )

        recursos = [
            "Pizarra y marcadores",
            "Cuaderno del estudiante y libro de texto",
            "Material concreto del entorno escolar (semillas, tapitas o reglas)",
            "Guía de trabajo impresa o copiada de la pizarra",
        ]

        evaluacion = {
            "procedimiento": ["Observación sistemática", "Prueba práctica escrita o formativa"],
            "instrumento": ["Rúbrica analítica", "Lista de cotejo de aula"],
            "indicadores": [
                f"Identifica los elementos centrales de {tema_sanitizado}.",
                "Aplica los pasos adecuados para resolver la consigna propuesta.",
                "Colabora de manera respetuosa en las actividades de equipo.",
            ],
        }

        adaptacion_tea = None
        if req.incluir_adaptacion_tea:
            adaptacion_tea = {
                "apoyos_visuales": "Agenda visual en pizarra con los 3 momentos de la clase y pictogramas.",
                "instrucciones": "Consignas redactadas paso a paso, en lenguaje directo, evitando dobles sentidos.",
                "pausas_sensoriales": "Permitir 2 pausas de 3 minutos para descanso sensorial o beber agua.",
                "evaluacion_diferenciada": "Presentar opciones con apoyo gráfico o respuesta oral sin presión de tiempo.",
            }

        return PlanLeccionResponse(
            tema=tema_sanitizado,
            materia=req.materia,
            grado=req.grado_o_curso,
            capacidad_mec=capacidad,
            inicio=inicio,
            desarrollo=desarrollo,
            cierre=cierre,
            recursos=recursos,
            evaluacion=evaluacion,
            adaptacion_tea=adaptacion_tea,
        )

    async def generar_rubrica(self, req: RubricaRequest) -> RubricaResponse:
        """Genera una rúbrica con criterios Logrado, En Proceso y No Logrado."""
        tema_clean = DataMinimizer.sanitize_text(req.tema)

        indicadores = [
            {
                "criterio": f"Comprensión conceptual de {tema_clean}",
                "logrado": f"Explica y aplica con claridad los fundamentos de {tema_clean}.",
                "en_proceso": f"Reconoce {tema_clean} pero requiere asistencia para aplicarlo.",
                "no_logrado": f"Presenta dificultades para identificar los conceptos básicos.",
            },
            {
                "criterio": "Resolución de consignas prácticas",
                "logrado": "Resuelve la totalidad de los ejercicios de forma autónoma y precisa.",
                "en_proceso": "Resuelve al menos la mitad de las actividades con orientación del docente.",
                "no_logrado": "No completa los ejercicios o comete errores metodológicos reiterados.",
            },
            {
                "criterio": "Comunicación y trabajo colaborativo",
                "logrado": "Expresa sus ideas con respeto y participa activamente en el aula.",
                "en_proceso": "Participa ocasionalmente cuando el docente lo convoca.",
                "no_logrado": "Muestra desinterés o interrumpe la dinámica de trabajo de sus pares.",
            },
        ]

        return RubricaResponse(tema=tema_clean, indicadores=indicadores)
