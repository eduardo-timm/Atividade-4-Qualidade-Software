"""Regras simples de pedidos do domínio LocalEats."""


def pedido_atingiu_valor_minimo(valor_pedido):
    """Aceita pedidos a partir de R$ 30; rejeita valores negativos.

    Responsável: Eduardo Timm Mendes.
    """
    if valor_pedido < 0:
        raise ValueError("O valor do pedido não pode ser negativo.")
    return valor_pedido >= 30


def calcular_desconto(valor_pedido):
    """Retorna 10% para pedidos a partir de R$ 100; abaixo disso, zero.

    Responsável: Tomas Madruga Flores.
    """
    if valor_pedido < 0:
        raise ValueError("O valor do pedido não pode ser negativo.")
    if valor_pedido < 100:
        return 0
    return valor_pedido * 0.10
