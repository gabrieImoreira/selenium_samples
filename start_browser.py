
# imports necessários para o selenium
from selenium import webdriver # importa o módulo webdriver do pacote selenium
from selenium.webdriver.chrome.options import Options # importa a classe Options do módulo chrome.options do pacote selenium
from webdriver_manager.chrome import ChromeDriverManager # importa a classe ChromeDriverManager do pacote webdriver_manager.chrome que é responsável por gerenciar o driver do Chrome
import time # importa o módulo time que é responsável por trabalhar com tempo

# imports possivelmente necessários
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Definindo função para criar um navegador
def create_browser(headless=False):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-logging")
    options.add_argument("--intl.accept_languages\=pt-BR")

    if headless:
        options.add_argument("--headless")

    browser = webdriver.Chrome(options=options)
    return browser



# chamando a funçção create_browser() e atribuindo o retorno a variável browser

# Define a URL
url='https://www.google.com'

browser = create_browser()
browser.get(url)
time.sleep(5)
