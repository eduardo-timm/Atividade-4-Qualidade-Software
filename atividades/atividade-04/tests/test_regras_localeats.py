"""Testes unitários das regras de pedidos."""

import pytest

from src.regras_localeats import calcular_desconto, pedido_atingiu_valor_minimo


# Responsável: Eduardo Timm Mendes
def test_pedido_acima_do_minimo_e_aceito():
    assert pedido_atingiu_valor_minimo(50) is True


# Responsável: Tomas Madruga Flores
def test_pedido_de_150_recebe_15_de_desconto():
    assert calcular_desconto(150) == 15


# Responsável: Eduardo Timm Mendes
def test_pedido_abaixo_de_30_e_recusado():
    assert pedido_atingiu_valor_minimo(29.99) is False


# Responsável: Tomas Madruga Flores
def test_pedido_abaixo_de_100_nao_recebe_desconto():
    assert calcular_desconto(99.99) == 0


# Responsável: Eduardo Timm Mendes
def test_pedido_de_exatamente_30_e_aceito():
    assert pedido_atingiu_valor_minimo(30) is True


# Responsável: Eduardo Timm Mendes
def test_pedido_negativo_gera_erro():
    with pytest.raises(ValueError, match="negativo"):
        pedido_atingiu_valor_minimo(-1)


# Responsável: Tomas Madruga Flores
def test_pedido_de_exatamente_100_recebe_10_de_desconto():
    assert calcular_desconto(100) == 10


# Responsável: Tomas Madruga Flores
def test_desconto_de_pedido_negativo_gera_erro():
    with pytest.raises(ValueError, match="negativo"):
        calcular_desconto(-1)
