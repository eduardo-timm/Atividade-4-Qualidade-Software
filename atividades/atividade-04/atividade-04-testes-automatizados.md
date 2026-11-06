# Atividade 4: Testes Automatizados do LocalEats

## 1. Identificação

| Campo | Informação |
| --- | --- |
| Unidade curricular | Qualidade de Software |
| Projeto | LocalEats |
| Modalidade | Dupla |
| Integrantes | Eduardo Timm Mendes e Tomas Madruga Flores |
| Sistema | [LocalEats](https://local-eats-unisenac.vercel.app/) |
| Data do registro | 06/11/2026 |

Foram implementadas duas funções Python, oito testes unitários e dois testes funcionais. Cada integrante possui uma regra e um fluxo funcional diferente. Os testes foram executados com pytest; os funcionais utilizaram Playwright com Chromium.

## 2. Regras implementadas

O código está em [src/regras_localeats.py](src/regras_localeats.py). As funções são exercícios locais do domínio do LocalEats; os testes funcionais acessam a aplicação publicada.

### Eduardo Timm Mendes — Regra 1: valor mínimo do pedido

Função: `pedido_atingiu_valor_minimo(valor_pedido)`.

- Valor igual ou superior a R$ 30,00: retorna `True`.
- Valor inferior a R$ 30,00: retorna `False`.
- Valor negativo: lança `ValueError`.

Os quatro testes verificam um pedido de R$ 50,00, um pedido de R$ 29,99, o limite exato de R$ 30,00 e um valor negativo.

### Tomas Madruga Flores — Regra 2: desconto do pedido

Função: `calcular_desconto(valor_pedido)`.

- Valor inferior a R$ 100,00: retorna desconto igual a zero.
- Valor igual ou superior a R$ 100,00: retorna 10% do valor informado.
- Valor negativo: lança `ValueError`.

Os quatro testes verificam desconto de R$ 15,00 para um pedido de R$ 150,00, ausência de desconto para R$ 99,99, desconto de R$ 10,00 no limite de R$ 100,00 e uma entrada negativa. O retorno é o desconto, e não o total a pagar.

## 3. Identificação das responsabilidades

| ID | Integrante | Tipo | Comportamento verificado | Arquivo e função |
| --- | --- | --- | --- | --- |
| TU01 | Eduardo Timm Mendes | Unitário | Pedido acima do mínimo é aceito | `tests/test_regras_localeats.py::test_pedido_acima_do_minimo_e_aceito` |
| TU02 | Eduardo Timm Mendes | Unitário | Pedido abaixo de R$ 30,00 é recusado | `tests/test_regras_localeats.py::test_pedido_abaixo_de_30_e_recusado` |
| TU03 | Eduardo Timm Mendes | Unitário | Limite exato de R$ 30,00 é aceito | `tests/test_regras_localeats.py::test_pedido_de_exatamente_30_e_aceito` |
| TU04 | Eduardo Timm Mendes | Unitário | Pedido negativo gera ValueError | `tests/test_regras_localeats.py::test_pedido_negativo_gera_erro` |
| TU05 | Tomas Madruga Flores | Unitário | R$ 150,00 recebem R$ 15,00 de desconto | `tests/test_regras_localeats.py::test_pedido_de_150_recebe_15_de_desconto` |
| TU06 | Tomas Madruga Flores | Unitário | Pedido abaixo de R$ 100,00 não recebe desconto | `tests/test_regras_localeats.py::test_pedido_abaixo_de_100_nao_recebe_desconto` |
| TU07 | Tomas Madruga Flores | Unitário | Limite exato de R$ 100,00 recebe 10% de desconto | `tests/test_regras_localeats.py::test_pedido_de_exatamente_100_recebe_10_de_desconto` |
| TU08 | Tomas Madruga Flores | Unitário | Cálculo de desconto com pedido negativo gera ValueError | `tests/test_regras_localeats.py::test_desconto_de_pedido_negativo_gera_erro` |
| TF01 | Eduardo Timm Mendes | Funcional | Login com credenciais inválidas exibe erro e mantém o acesso fechado | `tests/test_localeats.py::test_login_com_credenciais_invalidas_exibe_erro` |
| TF02 | Tomas Madruga Flores | Funcional | Cadastro vazio exige o nome e mantém o formulário aberto | `tests/test_localeats.py::test_cadastro_vazio_exige_nome_e_mantem_formulario_aberto` |

O pytest acrescenta `[chromium]` aos nomes dos testes funcionais no relatório, indicando o navegador utilizado.

## 4. Aplicação simplificada do TDD

Os ciclos abaixo foram executados durante a preparação da atividade com apoio de IA. As falhas intermediárias são intencionais e estão preservadas nas evidências; o código final passa nos testes.

### TDD de Eduardo Timm Mendes

- **Regra escolhida:** verificar valor mínimo do pedido.
- **Primeiro teste escrito:** `test_pedido_acima_do_minimo_e_aceito`, esperando `True` para R$ 50,00.
- **Por que o teste falhou inicialmente:** a função ainda lançava `NotImplementedError`.
- **Implementação mínima realizada:** retornar `True`, suficiente para o primeiro cenário. A execução seguinte aprovou o teste.
- **Segundo teste escrito:** `test_pedido_abaixo_de_30_e_recusado`, esperando `False` para R$ 29,99. Ele falhou porque a implementação retornava `True` para qualquer entrada.
- **Ajuste realizado:** substituir o retorno fixo por `valor_pedido >= 30`. Os dois cenários passaram.
- **Melhoria ou refatoração realizada:** adicionar teste do limite exato e teste de exceção com `pytest.raises`; após confirmar a falha da entrada negativa, incluir a validação com `ValueError`. A função ficou em um módulo separado, com documentação e identificação do responsável.

### TDD de Tomas Madruga Flores

- **Regra escolhida:** calcular o desconto do pedido.
- **Primeiro teste escrito:** `test_pedido_de_150_recebe_15_de_desconto`, esperando `15` para um pedido de R$ 150,00.
- **Por que o teste falhou inicialmente:** a função ainda lançava `NotImplementedError`.
- **Implementação mínima realizada:** retornar `valor_pedido * 0.10`. A execução seguinte aprovou o primeiro teste.
- **Segundo teste escrito:** `test_pedido_abaixo_de_100_nao_recebe_desconto`, esperando `0` para R$ 99,99. Ele falhou porque a função calculava 10% também abaixo do limite.
- **Ajuste realizado:** retornar zero quando `valor_pedido < 100`, mantendo o cálculo para os demais pedidos. Os dois cenários passaram.
- **Melhoria ou refatoração realizada:** acrescentar o teste do limite de R$ 100,00 e a verificação de `ValueError` para valores negativos. Após observar que a exceção não era lançada, incluir a validação antes do cálculo e documentar o retorno da função.

### Evidências dos ciclos

Os arquivos registram os testes dos dois integrantes em cada etapa.

| Etapa | Resultado observado | Evidência |
| --- | --- | --- |
| Primeiro Red | 2 falhas por funções não implementadas | [tdd-01-red.txt](evidencias/tdd-01-red.txt) |
| Primeiro Green | 2 testes aprovados com implementação mínima | [tdd-02-green.txt](evidencias/tdd-02-green.txt) |
| Segundo Red | 2 aprovados e 2 falhas nos novos cenários | [tdd-03-red.txt](evidencias/tdd-03-red.txt) |
| Segundo Green | 4 testes aprovados após os ajustes | [tdd-04-green.txt](evidencias/tdd-04-green.txt) |
| Exceções Red | 6 aprovados e 2 falhas pela ausência de ValueError | [tdd-05-red-excecoes.txt](evidencias/tdd-05-red-excecoes.txt) |
| Exceções Green | 8 testes unitários aprovados | [tdd-06-green.txt](evidencias/tdd-06-green.txt) |

## 5. Exploração e testes funcionais

Na exploração sem sessão autenticada, o endereço inicial apresentou a tela de acesso, com as opções **Entrar** e **Criar Conta**. Os fluxos escolhidos utilizam elementos encontrados nessa interface.

Os locators usam papéis e nomes dos botões, placeholders observados e IDs existentes nos formulários. Há dois botões chamados `Entrar`; por isso, o botão de envio é localizado dentro de `#loginForm`. Os campos não têm associação entre seus labels e inputs, então são localizados pelos placeholders reais. Cada teste recebe uma página e um contexto isolados, sem depender da execução do outro.

### TF01 — Login inválido — Eduardo Timm Mendes

1. Acessar o LocalEats e verificar a apresentação do formulário de login.
2. Preencher o e-mail fictício e a senha incorreta.
3. Clicar em **Entrar** dentro do formulário.
4. Verificar os resultados observáveis.

Assertions posteriores à interação:

- A mensagem de erro está visível.
- O texto da mensagem é exatamente `Invalid credentials`, conforme observado no site.
- O formulário de login continua visível.
- A URL permanece na página `/static/login.html`.

O cenário exercita a rejeição de uma tentativa de autenticação. O teste também confirma que a mensagem estava oculta antes do envio, evitando aprovar apenas um texto já presente na página.

### TF02 — Cadastro vazio — Tomas Madruga Flores

1. Acessar o LocalEats.
2. Clicar em **Criar Conta**.
3. Verificar que o formulário de cadastro aparece e o de login fica oculto.
4. Clicar em **Registrar** sem preencher os campos.
5. Verificar a validação do primeiro campo obrigatório.

Assertions posteriores à interação:

- O campo de nome recebe o foco.
- `validity.valueMissing` do campo de nome é `True`.
- O formulário de cadastro permanece visível.
- A mensagem de erro da aplicação permanece oculta.

O cenário verifica a validação nativa do navegador para o cadastro incompleto. O texto do balão de validação pode variar conforme o idioma do navegador; por isso, as verificações usam o foco e a propriedade de validade. O teste não conclui o registro de uma conta.

Os dois fluxos usam as esperas automáticas dos locators e das assertions do Playwright. Não há `time.sleep`, respostas simuladas ou alteração do código do site.

## 6. Explicações individuais dos testes

### Eduardo Timm Mendes — explicação do TU03

O teste `test_pedido_de_exatamente_30_e_aceito` chama a função com o valor `30` e verifica `assert resultado is True`, expresso diretamente sobre a chamada no código. Esse valor representa a fronteira da regra: pedidos de R$ 30,00 já devem ser aceitos. Se a implementação usasse `> 30` em vez de `>= 30`, esse teste falharia, mesmo que o cenário de R$ 50,00 continuasse passando. Como a função não acessa rede ou banco de dados, o teste é unitário e independente.

### Tomas Madruga Flores — explicação do TU08

O teste `test_desconto_de_pedido_negativo_gera_erro` chama `calcular_desconto(-1)` dentro de `pytest.raises(ValueError, match="negativo")`. Ele só passa quando a função lança o tipo de exceção esperado e a mensagem contém `negativo`. Sem essa verificação, um valor negativo poderia retornar zero por estar abaixo de R$ 100,00, escondendo uma entrada inválida. O teste confirma que a validação acontece antes da aplicação da faixa de desconto.

## 7. Execução e relatório

Ambiente verificado: Windows, Python 3.15.2, pytest 9.2.0, Playwright 1.64.1 e pytest-playwright 0.10.0. As dependências estão fixadas em [requirements.txt](requirements.txt). O comando `python -m pip check` informou que não há dependências incompatíveis instaladas.

### Como reproduzir no PowerShell

Executar os comandos abaixo a partir da raiz do projeto, que contém a pasta `atividades`:

```powershell
python -m venv .venv
$env:PATH = (Resolve-Path '.venv/Scripts').Path + ';' + $env:PATH
Set-Location atividades/atividade-04
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m pytest -v | Tee-Object -FilePath relatorio-pytest.txt
```

Na pasta entregue, o ambiente `.venv` já foi preparado na raiz. A alteração de `PATH` acima seleciona esse Python apenas para a sessão atual do PowerShell. Os testes funcionais precisam de conexão com o site.

O arquivo [pytest.ini](pytest.ini) seleciona Chromium e habilita screenshots e traces. O comando de execução utilizado foi o solicitado no enunciado:

```powershell
python -m pytest -v | Tee-Object -FilePath relatorio-pytest.txt
```

### Resultado observado

| Tipo | Coletados | Aprovados | Reprovados |
| --- | --- | --- | --- |
| Unitários | 8 | 8 | 0 |
| Funcionais | 2 | 2 | 0 |
| **Total** | **10** | **10** | **0** |

O [relatorio-pytest.txt](relatorio-pytest.txt) contém a coleta, o resultado de cada teste e o resumo final. Todos os testes da tabela de responsabilidades aparecem nele. A execução também emitiu um aviso de depreciação de fixture na integração pytest/Playwright; o aviso está preservado no relatório e não ocasionou reprovação.

### Evidências funcionais

Os arquivos abaixo foram gerados pela execução final dos testes:

- TF01: [screenshot do login inválido](evidencias/playwright/tests-test-localeats-py-test-login-com-credenciais-invalidas-exibe-erro-chromium/test-finished-1.png) e [trace](evidencias/playwright/tests-test-localeats-py-test-login-com-credenciais-invalidas-exibe-erro-chromium/trace.zip).
- TF02: [screenshot da validação de cadastro](evidencias/playwright/tests-test-localeats-py-test-cadastro-vazio-exige-nome-e-mantem-formulario-aberto-chromium/test-finished-1.png) e [trace](evidencias/playwright/tests-test-localeats-py-test-cadastro-vazio-exige-nome-e-mantem-formulario-aberto-chromium/trace.zip).

Para abrir um trace, executar na pasta da atividade:

```powershell
python -m playwright show-trace "evidencias/playwright/tests-test-localeats-py-test-login-com-credenciais-invalidas-exibe-erro-chromium/trace.zip"
```

Cada nova execução substitui as evidências funcionais da execução anterior. Após alterar o código, é necessário executar novamente o comando que gera o relatório.

## 8. Diferenciais implementados

- Testes adicionais de limite para as duas regras.
- Verificação de exceções com `pytest.raises`.
- Registro real das falhas e aprovações dos ciclos de TDD.
- Screenshots e traces dos dois testes funcionais.
- Contextos isolados, locators específicos e assertions com espera automática.

## 9. Uso de inteligência artificial

**Ferramenta utilizada:** Codex, da OpenAI.

**Como a ferramenta foi utilizada:** leitura do enunciado, organização dos arquivos e responsabilidades, elaboração das funções e dos testes, execução dos ciclos de TDD, exploração do site com Playwright, execução da suíte e preparação deste documento.

**Uma sugestão que precisou ser alterada ou rejeitada:** durante a exploração, foi tentado localizar `LocalEats` como um título com `get_by_role("heading")`. A busca falhou porque o nome da aplicação está em um link, conforme o HTML real. A exploração foi corrigida para `get_by_role("link", name="LocalEats", exact=True)`. Os testes entregues utilizam os formulários e botões efetivamente encontrados na página.

**Como o código sugerido foi verificado:** execução real dos testes com pytest, conferência das falhas esperadas durante o TDD, execução dos dois fluxos no site publicado, inspeção dos screenshots, registro dos traces e comparação dos testes existentes com a tabela e com o relatório final.

A execução técnica foi realizada com apoio da ferramenta. Antes da entrega, Eduardo e Tomas devem revisar o código e conseguir explicar os testes atribuídos a cada um, conforme solicitado no enunciado.

## 10. Organização da entrega

```text
atividades/atividade-04/
├── atividade-04-testes-automatizados.md
├── relatorio-pytest.txt
├── requirements.txt
├── pytest.ini
├── src/
│   ├── __init__.py
│   └── regras_localeats.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_regras_localeats.py
│   └── test_localeats.py
└── evidencias/
    ├── tdd-*.txt
    ├── exploracao-*.png
    └── playwright/
        └── .../ (screenshots e traces por teste)
```

Para o Blackboard, publicar os arquivos no GitHub, garantir o acesso do professor e enviar o link direto para `atividades/atividade-04/atividade-04-testes-automatizados.md`.
