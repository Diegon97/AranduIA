from src.core.security import DataMinimizer


def test_sanitize_emails():
    raw = "Mi nombre es Juan y mi correo es juanito123@gmail.com para la tarea"
    clean = DataMinimizer.sanitize_text(raw)
    assert "juanito123@gmail.com" not in clean
    assert "[CORREO_PROTEGIDO]" in clean


def test_sanitize_paraguayan_phone():
    raw = "Escribime al 0981 123 456 o al +595971987654 para pasarme el ejercicio"
    clean = DataMinimizer.sanitize_text(raw)
    assert "0981" not in clean
    assert "+595971" not in clean
    assert "[TELEFONO_PROTEGIDO]" in clean


def test_sanitize_cedula():
    raw = "Mi número de cédula es C.I. 4.567.890 para el registro"
    clean = DataMinimizer.sanitize_text(raw)
    assert "4.567.890" not in clean
    assert "[CEDULA_PROTEGIDA]" in clean


def test_audit_payload():
    payload = {
        "tema": "Matemática",
        "telefono": "0981123456",
        "email": "test@escuela.edu.py",
        "consulta": "Escribime a profe@escuela.com"
    }
    audited = DataMinimizer.audit_payload(payload)
    assert "telefono" not in audited
    assert "email" not in audited
    assert audited["tema"] == "Matemática"
    assert "[CORREO_PROTEGIDO]" in audited["consulta"]
