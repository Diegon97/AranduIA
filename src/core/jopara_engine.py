"""
Motor de Bilingüismo y Cultura Jopara — AranduIA.
Provee soporte para Guaraní Jopara, léxico educativo y frases de aliento cultural.
"""

from typing import Dict, List, Optional
import random


class JoparaEngine:
    """Gestiona el vocabulario educativo, frases pedagógicas y detección de Jopara."""

    # Vocabulario pedagógico bilingüe
    GLOSARIO: Dict[str, Dict[str, str]] = {
        "aprender": {"guarani": "ñemoarandu", "significado": "hacerse sabio / estudiar"},
        "enseñar": {"guarani": "mbo'e", "significado": "guiar / instruir"},
        "profesor": {"guarani": "mbo'ehára", "significado": "maestro / docente"},
        "estudiante": {"guarani": "temimbo'e", "significado": "aprendiz / alumno"},
        "escuela": {"guarani": "mbo'ehao", "significado": "casa de enseñanza"},
        "libro": {"guarani": "aranduka", "significado": "libro / compendio de saber"},
        "leer": {"guarani": "moñe'ẽ", "significado": "hacer hablar al texto"},
        "escribir": {"guarani": "hai", "significado": "dibujar letras / redactar"},
        "numero": {"guarani": "papapy", "significado": "cifra o número"},
        "sumar": {"guarani": "mbojoapy", "significado": "añadir / unir"},
        "restar": {"guarani": "mboguevi", "significado": "retroceder / quitar"},
        "multiplicar": {"guarani": "mboheta", "significado": "hacer mucho / multiplicar"},
        "dividir": {"guarani": "mboja'o", "significado": "repartir en partes"},
        "pregunta": {"guarani": "porandu", "significado": "interrogación / consulta"},
        "respuesta": {"guarani": "mbohovái", "significado": "devolución / solución"},
        "sabiduria": {"guarani": "arandu", "significado": "conocimiento profundo"},
    }

    # Frases de aliento y motivación socrática en Jopara
    ALIENTOS: List[str] = [
        "¡Iporãiterei! Eñeha'ã porãiterei hína.",
        "¡Cháke, estás muy cerca! Miremos el siguiente paso.",
        "¡Jaha hese! Pasito a pasito vamos a llegar a la solución.",
        "¡Terehupyty nde potapy! Pensá con calma, vos podés.",
        "¡Ndaha'éi mba'eve! Equivocarse es la mejor forma de aprender.",
        "¡Emañami porã! Fijate bien en este detalle.",
    ]

    # Palabras clave para detectar expresión o intención en Guaraní / Jopara
    PALABRAS_CLAVE_JOPARA = {
        "mba'e", "mbae", "porã", "pora", "guaraní", "guarani", "jopara", 
        "mbo'e", "mboe", "mbo'ehara", "temimbo'e", "mbo'ehao", "arandu",
        "ikatu", "ndikati", "che", "nde", "ha'e", "ore", "peẽ", "ha'ekuéra",
        "tereho", "jaha", "ko'ẽ", "ka'aru", "pyhare", "moñe'ẽ", "hai",
        "chipa", "tereré", "terere", "mba'eichapa", "mbaeichapa"
    }

    @classmethod
    def detectar_jopara(cls, texto: str) -> bool:
        """Determina si un mensaje contiene palabras o intención en Jopara."""
        if not texto:
            return False
        tokens = set(texto.lower().replace("?", "").replace("!", "").split())
        return len(tokens.intersection(cls.PALABRAS_CLAVE_JOPARA)) > 0

    @classmethod
    def frase_aliento(cls) -> str:
        """Retorna una frase cálida de aliento pedagógico."""
        return random.choice(cls.ALIENTOS)

    @classmethod
    def buscar_termino(cls, termino: str) -> Optional[Dict[str, str]]:
        """Busca un término pedagógico en el glosario bilingüe."""
        term_clean = termino.lower().strip()
        return cls.GLOSARIO.get(term_clean)
