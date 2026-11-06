"""Fluxos públicos observados na interface real do LocalEats."""

import re

from playwright.sync_api import Page, expect


URL_LOCALEATS = "https://local-eats-unisenac.vercel.app/"


# Responsável: Eduardo Timm Mendes
def test_login_com_credenciais_invalidas_exibe_erro(page: Page):
    page.goto(URL_LOCALEATS, wait_until="domcontentloaded")
    formulario_login = page.locator("#loginForm")
    mensagem_erro = page.locator("#errorMsg")
    expect(formulario_login).to_be_visible()
    expect(mensagem_erro).to_be_hidden()

    # O domínio .invalid é reservado e evita usar o e-mail de uma pessoa real.
    page.get_by_placeholder("teste@teste.com", exact=True).fill(
        "usuario-inexistente-atividade04@example.invalid"
    )
    page.get_by_placeholder("Sua senha secreta", exact=True).fill(
        "senha-incorreta-atividade04"
    )
    formulario_login.get_by_role("button", name="Entrar", exact=True).click()

    expect(mensagem_erro).to_be_visible(timeout=15000)
    expect(mensagem_erro).to_have_text("Invalid credentials")
    expect(formulario_login).to_be_visible()
    expect(page).to_have_url(re.compile(r"/static/login\.html$"))


# Responsável: Tomas Madruga Flores
def test_cadastro_vazio_exige_nome_e_mantem_formulario_aberto(page: Page):
    page.goto(URL_LOCALEATS, wait_until="domcontentloaded")
    formulario_cadastro = page.locator("#registerForm")
    nome = page.get_by_placeholder("Seu nome", exact=True)
    expect(formulario_cadastro).to_be_hidden()

    page.get_by_role("button", name="Criar Conta", exact=True).click()
    expect(formulario_cadastro).to_be_visible()
    expect(page.locator("#loginForm")).to_be_hidden()

    formulario_cadastro.get_by_role("button", name="Registrar", exact=True).click()

    # Validação nativa observada: o navegador foca o primeiro campo obrigatório.
    expect(nome).to_be_focused()
    assert nome.evaluate("campo => campo.validity.valueMissing") is True
    expect(formulario_cadastro).to_be_visible()
    expect(page.locator("#errorMsg")).to_be_hidden()
