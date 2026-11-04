from unittest.mock import patch

def verificar_permissao(usuario: str) -> bool:
    return False

def acessar_sistema(usuario: str) -> str:
    if verificar_permissao(usuario):
        return "Acesso autorizado"
    return "Acesso negado"


@patch(f"{__name__}.verificar_permissao")
def test_usuario_com_permissao(mock_verificar):
    mock_verificar.return_value = True
    assert acessar_sistema("Carlos") == "Acesso autorizado"

@patch(f"{__name__}.verificar_permissao")
def test_usuario_sem_permissao(mock_verificar):
    mock_verificar.return_value = False
    assert acessar_sistema("Carlos") == "Acesso negado"

@patch(f"{__name__}.verificar_permissao")
def test_verificar_se_permissao_foi_chamada(mock_verificar):
    mock_verificar.return_value = True
    acessar_sistema("Carlos")
    mock_verificar.assert_called()

@patch(f"{__name__}.verificar_permissao")
def test_verificar_se_chamada_com_usuario_correto(mock_verificar):
    mock_verificar.return_value = True
    acessar_sistema("Carlos")
    mock_verificar.assert_called_once_with("Carlos")

@patch(f"{__name__}.verificar_permissao")
def test_simular_dois_cenarios(mock_verificar):
    mock_verificar.return_value = True
    assert acessar_sistema("Admin") == "Acesso autorizado"

    mock_verificar.return_value = False
    assert acessar_sistema("Visitante") == "Acesso negado"