from unittest.mock import patch

def obter_proximo_cliente():
    return None

def registrar_atendimento(cliente: str) -> bool:
    return True

def atender_proximo_cliente() -> str:
    cliente = obter_proximo_cliente()
    if not cliente:
        return "Fila vazia"
    
    sucesso = registrar_atendimento(cliente)
    if sucesso:
        return "Atendimento realizado"
    return "Falha no atendimento"


@patch(f"{__name__}.registrar_atendimento")
@patch(f"{__name__}.obter_proximo_cliente")
def test_atendimento_realizado_com_sucesso(mock_obter, mock_registrar):
    mock_obter.return_value = "Carlos"
    mock_registrar.return_value = True
    assert atender_proximo_cliente() == "Atendimento realizado"

@patch(f"{__name__}.registrar_atendimento")
@patch(f"{__name__}.obter_proximo_cliente")
def test_fila_vazia(mock_obter, mock_registrar):
    mock_obter.return_value = None
    assert atender_proximo_cliente() == "Fila vazia"

@patch(f"{__name__}.registrar_atendimento")
@patch(f"{__name__}.obter_proximo_cliente")
def test_falha_ao_registrar_atendimento(mock_obter, mock_registrar):
    mock_obter.return_value = "Carlos"
    mock_registrar.return_value = False
    assert atender_proximo_cliente() == "Falha no atendimento"

@patch(f"{__name__}.registrar_atendimento")
@patch(f"{__name__}.obter_proximo_cliente")
def test_verificar_se_obter_proximo_cliente_foi_chamada(mock_obter, mock_registrar):
    mock_obter.return_value = "Carlos"
    mock_registrar.return_value = True
    atender_proximo_cliente()
    mock_obter.assert_called_once()

@patch(f"{__name__}.registrar_atendimento")
@patch(f"{__name__}.obter_proximo_cliente")
def test_verificar_se_registrar_atendimento_chamado_com_cliente_correto(mock_obter, mock_registrar):
    mock_obter.return_value = "Carlos"
    mock_registrar.return_value = True
    atender_proximo_cliente()
    mock_registrar.assert_called_once_with("Carlos")

@patch(f"{__name__}.registrar_atendimento")
@patch(f"{__name__}.obter_proximo_cliente")
def test_registrar_atendimento_nao_chamado_quando_fila_vazia(mock_obter, mock_registrar):
    mock_obter.return_value = None
    atender_proximo_cliente()
    mock_registrar.assert_not_called()