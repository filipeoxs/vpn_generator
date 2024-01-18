# Import necessary modules from Selenium and other libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from read_configs import read_configs

# Get URLs, username, and password from the configuration file
cloud_datas = read_configs()
url_cloud = f'http://{cloud_datas[4]}'
username = cloud_datas[5]
password = cloud_datas[6]

# Configure Chrome options to disable SSL certificate verification
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

# Initialize the Chrome browser with configured options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the first URL
driver.get(url_cloud)

# Locate the input element for username using the name attribute and enter the username
element_input_user = driver.find_element(By.NAME, 'user').send_keys(username)

# Locate the input element for password using the name attribute and enter the password
element_input_password = driver.find_element(By.NAME, 'password').send_keys(password)

# Click the login button using the element ID
driver.find_element(By.ID,'submit').click()

# Navigate to a specific folder in the cloud
driver.get('https://nuvem.ipea.gov.br/index.php/apps/files/?dir=/VPN%20usu%C3%A1rios%20IPEA&fileid=2606571')

# Create a new folder by clicking on the 'New' button
driver.find_element(By.CLASS_NAME, 'button new').click()

# Click on the option to create a new folder from the context menu
driver.find_element(By.XPATH, '//*[@id="body-user"]/div[6]/ul/li[2]/a').click()

# Enter the name of the new folder in the input field
driver.find_element(By.ID, 'view11-input-folder').send_keys('teste')

# Pause execution for 30 seconds
time.sleep(30)

# Close the browser
driver.quit()
