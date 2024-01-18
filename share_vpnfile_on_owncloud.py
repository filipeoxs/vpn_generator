from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from read_configs import read_configs

# Get URLs from the configuration file
cloud_datas = read_configs()
url_cloud = f'http://{cloud_datas[4]}'
username = cloud_datas[5]
password = cloud_datas[6]

# Configure Chrome options to disable SSL certificate verification
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

# Initialize the browser with configured options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the first URL
driver.get(url_cloud)

# Locate the input element by name using By.NAME
element_input_user = driver.find_element(By.NAME, 'user').send_keys(username)

# Locate the input element by name using By.NAME
element_input_password = driver.find_element(By.NAME, 'password').send_keys(password)

driver.find_element(By.ID,'submit').click()

# Perform necessary operations...
# Go to the folder users vpns ipea
driver.get('https://nuvem.ipea.gov.br/index.php/apps/files/?dir=/VPN%20usu%C3%A1rios%20IPEA&fileid=2606571')

# Create a new folder
driver.find_element(By.CLASS_NAME, 'button new').click()
driver.find_element(By.XPATH, '//*[@id="body-user"]/div[6]/ul/li[2]/a').click()
# Inform the name of the folder
driver.find_element(By.ID, 'view11-input-folder').send_keys('teste')


time.sleep(30)
# Close the browser
driver.quit()