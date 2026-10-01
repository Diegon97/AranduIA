"""
Módulo de Seguridad y Privacidad Infantil — Cumplimiento de la Ley N° 7593/2025 de Paraguay.
Aplica principios de minimización, anonimización y sanitización estricta antes de inferencia.
"""

import re
from typing import Dict, Any


class DataMinimizer:
    """Sanitiza y anonimiza textos para proteger datos de menores y docentes."""

    # Regex para Cédulas de Identidad paraguayas (ej: 1.234.567, 1234567, con o sin puntos)
    CEDULA_REGEX = re.compile(r"\b\d{1,2}(?:\.\d{3}){2}\b|\b\d{6,8}\b")

    # Regex para números telefónicos (móviles paraguayos 0981..., +5959..., etc.)
    PHONE_REGEX = re.compile(
        r"(?:\+?595\s?|0)?9\d{2}[-\s]?\d{3}[-\s]?\d{3}\b"
    )

    # Regex para correos electrónicos
    EMAIL_REGEX = re.compile(
        r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    )

    @classmethod
    def sanitize_text(cls, text: str) -> str:
        """Elimina identificadores personales directos de cualquier texto."""
        if not text:
            return ""

        sanitized = cls.EMAIL_REGEX.sub("[CORREO_PROTEGIDO]", text)
        sanitized = cls.PHONE_REGEX.sub("[TELEFONO_PROTEGIDO]", sanitized)
        # Solo sanitizamos números largos que parezcan CI si van precedidos de CI, C.I., cedula o tienen formato con puntos
        sanitized = re.sub(
            r"(?:c\.?i\.?|c[ée]dula|identidad)\s*[:#]?\s*(\d[\d\.]*)",
            "[CEDULA_PROTEGIDA]",
            sanitized,
            flags=re.IGNORECASE,
        )

        return sanitized

    @classmethod
    def audit_payload(cls, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Asegura que ninguna petición contenga campos prohibidos."""
        forbidden_keys = {"ci", "cedula", "telefono", "phone", "email", "direccion", "location", "apellido"}
        clean = {}
        for k, v in payload.items():
            if k.lower() in forbidden_keys:
                continue
            if isinstance(v, str):
                clean[k] = cls.sanitize_text(v)
            elif isinstance(v, dict):
                clean[k] = cls.audit_payload(v)
            else:
                clean[k] = v
        return clean
