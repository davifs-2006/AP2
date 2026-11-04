from unittest.mock import patch

def gerar_codigo() -> str:
    return "USR-1234"

def criar_identificacao(nome: str) -> str:
    codigo = gerar_codigo()
    return f"Usuário {nome} cadastrado com código {codigo}."


@patch(f"{__name__}.gerar_codigo")
def test_mensagem_gerada_corretamente(mock_gerar_codigo):
    mock_gerar_codigo.return_value = "USR-1234"
    mensagem = criar_identificacao("Carlos")
    assert mensagem == "Usuário Carlos cadastrado com código USR-1234."

@patch(f"{__name__}.gerar_codigo")
def test_verificar_se_gerar_codigo_foi_chamada(mock_gerar_codigo):
    mock_gerar_codigo.return_value = "USR-1234"
    criar_identificacao("Carlos")
    mock_gerar_codigo.assert_called()

@patch(f"{__name__}.gerar_codigo")
def test_verificar_se_chamada_apenas_uma_vez(mock_gerar_codigo):
    mock_gerar_codigo.return_value = "USR-1234"
    criar_identificacao("Carlos")
    mock_gerar_codigo.assert_called_once()

@patch(f"{__name__}.gerar_codigo")
def test_simular_diferentes_codigos_com_mock(mock_gerar_codigo):
    mock_gerar_codigo.return_value = "USR-9999"
    assert criar_identificacao("Carlos") == "Usuário Carlos cadastrado com código USR-9999."

@patch(f"{__name__}.gerar_codigo")
def test_comportamento_com_nomes_diferentes(mock_gerar_codigo):
    mock_gerar_codigo.return_value = "USR-1234"
    assert criar_identificacao("Ana") == "Usuário Ana cadastrado com código USR-1234."
    assert criar_identificacao("João") == "Usuário João cadastrado com código USR-1234."
