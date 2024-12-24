import pytest

def pytest_addoption(parser):
    """Adiciona a opção de linha de comando --browser ao pytest."""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Navegador para rodar os testes: chrome, firefox ou safari",
    )

@pytest.fixture
def browser(request):
    """Lê o navegador da linha de comando."""
    return request.config.getoption("--browser")