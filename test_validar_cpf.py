def validar_documento(documento: str) -> bool:
    if not documento:
        return False
    doc_limpo = documento.replace(".", "").replace("-", "")
    return doc_limpo.isdigit() and len(doc_limpo) == 11


def test_documento_com_11_digitos():
    assert validar_documento("12345678901") is True

def test_documento_formatado():
    assert validar_documento("123.456.789-00") is True

def test_documento_com_menos_de_11_digitos():
    assert validar_documento("123456789") is False

def test_documento_com_mais_de_11_digitos():
    assert validar_documento("123456789012") is False

def test_documento_contendo_letras():
    assert validar_documento("123.456.789-XX") is False

def test_documento_vazio():
    assert validar_documento("") is False
