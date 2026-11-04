import pytest
from unittest.mock import patch

def classificar_produto(quantidade: int) -> str:
    if quantidade < 0:
        return "Quantidade inválida"
    elif quantidade == 0:
        return "Sem estoque"
    elif 1 <= quantidade <= 5:
        return "Estoque baixo"
    elif 6 <= quantidade <= 20:
        return "Estoque normal"
    else:
        return "Estoque alto"


def test_produto_sem_estoque():
    assert classificar_produto(0) == "Sem estoque"

def test_produto_estoque_baixo():
    assert classificar_produto(3) == "Estoque baixo"

def test_produto_estoque_normal():
    assert classificar_produto(10) == "Estoque normal"

def test_produto_estoque_alto():
    assert classificar_produto(25) == "Estoque alto"

def test_quantidade_negativa():
    assert classificar_produto(-5) == "Quantidade inválida"

