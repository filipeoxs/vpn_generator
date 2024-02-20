from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from read_configs import read_configs
import time




# Get URLs from the configuration file
urls = read_configs()
urlvpn1 = urls[2]

# Get the second URL from the configuration file
urlvpn2 = f'http://{urls[3]}'

def login():
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--safebrowsing-disable-download-protection")
    chrome_options.add_argument("--unlimited-storage")
    #chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(urlvpn1)
    driver.find_element(By.NAME, 'usernamefld').send_keys(urls[9])
    driver.find_element(By.NAME, 'passwordfld').send_keys(urls[8])
    driver.find_element(By.NAME, 'login').click()
    return driver

def search_certificate(username):
    try:
        driver = login()
        driver.get('https://vpn1.ipea.gov.br/system_certmanager.php')
        nome_elemento = driver.find_element(By.XPATH, "//*[@id='3']/div/div[3]/div[2]/div/table/tbody")
        trs = nome_elemento.find_elements(By.TAG_NAME, 'tr')

        for tr in trs:
            username_info = " ".join(line.strip() for line in tr.text.splitlines() if line.strip())
            username_cert_name = username_info.split(' CA')[0].strip()
            
            if username_cert_name == username:
                pos_from = username_info.find('Valid From:')
                pos_until = username_info.find('Valid Until:')
                valid_from = None
                valid_until = None

                if pos_from != -1 and pos_until != -1:
                    valid_from = username_info[pos_from + len('Valid From:'):pos_until].strip()
                    valid_until = username_info[pos_until + len('Valid Until:'):].strip()

                    valid_from = valid_from.replace("webConfigurator", "").replace("OpenVPN Server", "")
                    valid_until = valid_until.replace("webConfigurator", "").replace("OpenVPN Server", "")

                    valid_from = datetime.strptime(valid_from, "%a, %d %b %Y %H:%M:%S %z").strftime("%d/%m/%Y %H:%M:%S")
                    valid_until = datetime.strptime(valid_until, "%a, %d %b %Y %H:%M:%S %z").strftime("%d/%m/%Y %H:%M:%S")

                return username_cert_name, valid_from, valid_until
    except Exception as e:
        print(f"Erro na busca do certificado: {e}")
    finally:
        driver.quit()
        
def download_vpn(username):
    try:
        driver = login()
        driver.get('https://vpn1.ipea.gov.br/vpn_openvpn_export.php')
        # Localizar o elemento pelo nome "server"
        select_element = driver.find_element(By.NAME, "server")

        # Criar um objeto Select para interagir com a lista suspensa
        select = Select(select_element)

        # Selecionar a opção desejada (por valor)
        select.select_by_value("4")  # Isso seleciona a opção com o valor "OpenVPN Acesso Usuario UDP4:1197"
        nome_elemento = driver.find_element(By.XPATH, "//*[@id='users']")
        trs = nome_elemento.find_elements(By.TAG_NAME, 'tr')
        
        # Usuário específico que você está procurando
        usuario_especifico = "t05613226199"  # Substitua pelo usuário desejado

        for tr in trs:
            username_info = " ".join(line.strip() for line in tr.text.splitlines() if line.strip())
            username_cert_name = username_info.split(' Certificate with External Auth')[0].strip()

            # Verificar se o usuário específico está presente na linha
            if usuario_especifico in username_cert_name:
                print(f"Usuário {usuario_especifico} encontrado na linha:")
                print(username_info)
                print('\n')

                # Encontrar o link para o botão desejado dentro do tr específico
                tr.find_element(By.XPATH, ".//a[contains(@href, 'inst-Win10')]").click()
                
                # Clicar no link do botão usando JavaScript
                #driver.execute_script("arguments[0].click();", button_link)
                # Aguardar um curto período para garantir que o JavaScript tenha tempo para executar
                time.sleep(20)

                # Obter a URL da nova janela (ou aba) que foi aberta pelo JavaScript
                #new_window_url = driver.current_url

                # Utilizar requests para fazer o download do arquivo
                '''try:
                    response = requests.get(link, stream=True, verify= False)

                    # Verificar se o download foi bem-sucedido
                    if response.status_code == 200:
                        # Especificar o caminho local para salvar o arquivo
                        local_filename = f"{os.getcwd()}/tmp/vpn_{usuario_especifico}"

                        # Salvar o conteúdo do arquivo localmente
                        with open(local_filename, 'wb') as file:
                            for chunk in response.iter_content(chunk_size=128):
                                file.write(chunk)

                        print(f"Arquivo baixado com sucesso em: {local_filenasvdflg201044me}")
                    else:
                        print(f"Erro ao baixar o arquivo. Código de status: {response.status_code}")
                except Exception as error_download_vpn:
                    print(f"Erro no download do certificado: {error_download_vpn}")
                finally:
                    driver.quit()'''
                break
    except Exception as error_download_vpn:
        print(f"Erro no download do certificado: {error_download_vpn}")
'''    finally:
        driver.quit()'''