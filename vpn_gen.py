from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from read_configs import read_configs

# Obtenha as URLs do arquivo de configuração
urls = read_configs()
urlvpn1 = f'http://{urls[2]}'
time.sleep(10)
urlvpn2 = f'http://{urls[3]}'

# Configurar opções do Chrome para desativar a verificação do certificado SSL
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
capabilities = {
    'acceptInsecureCerts': True
}

# Inicializar o navegador com as opções configuradas
browser = webdriver.Chrome(options=chrome_options, capabilities=capabilities)

# Navegar para a primeira URL
browser.get(urlvpn1)

# Realizar as operações necessárias...

# Fechar o navegador
browser.quit()
