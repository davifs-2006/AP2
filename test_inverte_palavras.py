def inverter_palavras(texto: str) -> str:
    if not texto or not texto.strip():
        return ""
    palavras = texto.split()
    return " ".join(reversed(palavras))


def test_frase_com_varias_palavras():
    assert inverter_palavras("Python é muito interessante") == "interessante muito é Python"

def test_frase_com_apenas_uma_palavra():
    assert inverter_palavras("Python") == "Python"

def test_frase_vazia():
    assert inverter_palavras("") == ""

def test_frase_com_espacos_extras():
    assert inverter_palavras("   Python   é   muito   interessante   ") == "interessante muito é Python"

def test_frase_com_numeros_e_letras():
    assert inverter_palavras("Teste 123 456 ok") == "ok 456 123 Teste"