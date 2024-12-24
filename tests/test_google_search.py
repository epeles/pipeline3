from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest


@pytest.fixture(params=["chrome", "firefox", "safari"])
def driver(request):
    """Configura o WebDriver para diferentes navegadores."""
    browser = request.param

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(
            service=webdriver.chrome.service.Service(ChromeDriverManager().install()),
            options=options
        )

    elif browser == "firefox":
        options = FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(
            service=webdriver.firefox.service.Service(GeckoDriverManager().install()),
            options=options
        )

    elif browser == "safari":
        driver = webdriver.Safari()
        # Safari não suporta modo headless diretamente

    else:
        raise ValueError(f"Navegador {browser} não é suportado.")

    yield driver
    driver.quit()


def test_google_search(driver):
    """Teste para buscar um termo no Google e verificar o título da página."""
    driver.get("https://www.google.com")
    
    # Espera até que o campo de busca esteja presente
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    
    # Digita a busca e envia
    search_box.send_keys("GitHub Copilot")
    search_box.send_keys(Keys.RETURN)

    # Verifica que o título contém o termo pesquisado
    WebDriverWait(driver, 10).until(
        EC.title_contains("GitHub Copilot")
    )
    assert "GitHub Copilot" in driver.title, "O título não contém 'GitHub Copilot'"