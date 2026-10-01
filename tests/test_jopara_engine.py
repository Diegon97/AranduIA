from src.core.jopara_engine import JoparaEngine


def test_jopara_detection():
    assert JoparaEngine.detectar_jopara("Mba'éichapa nde ko'ẽ") is True
    assert JoparaEngine.detectar_jopara("Hola, ¿cómo estás?") is False
    assert JoparaEngine.detectar_jopara("Quiero aprender con che mbo'ehara") is True


def test_glosario_lookup():
    termino = JoparaEngine.buscar_termino("aprender")
    assert termino is not None
    assert termino["guarani"] == "ñemoarandu"

    termino_sumar = JoparaEngine.buscar_termino("sumar")
    assert termino_sumar is not None
    assert termino_sumar["guarani"] == "mbojoapy"


def test_frase_aliento():
    frase = JoparaEngine.frase_aliento()
    assert len(frase) > 5
