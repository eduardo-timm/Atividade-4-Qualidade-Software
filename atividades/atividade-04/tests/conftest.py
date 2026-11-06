"""Configuração compartilhada; cada teste recebe um contexto isolado."""

import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "locale": "pt-BR",
        "viewport": {"width": 1440, "height": 1000},
    }
