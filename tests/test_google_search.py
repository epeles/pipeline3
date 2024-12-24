from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture
def driver():
    """Configura o WebDriver para o Chrome."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Executa sem interface gráfica
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service,options=chrome_options)
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