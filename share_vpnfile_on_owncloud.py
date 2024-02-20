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

time.sleep(2)

# Create a new folder by clicking on the 'New' button
driver.find_element(By.XPATH, '//*[@id="controls"]/div[3]/a').click()
time.sleep(2)

# Click on the option to create a new folder from the context menu
driver.find_element(By.XPATH, '//*[@id="body-user"]/div[6]/ul/li[2]/a').click()
time.sleep(2)

create_folder_driver = driver.find_element(By.ID, 'view11-input-folder')
# Enter the name of the new folder in the input field
create_folder_driver.send_keys('teste')
create_folder_driver.send_keys(Keys.ENTER)
time.sleep(2)

# Search for the folder with the name of the user
folder_with_user_name = driver.find_element(By.XPATH, '//*[@id="fileList"]//td[@class="filename ui-draggable"]/a[@class="name" and .//span[@class="innernametext" and text()="teste"]]')
# Click on the folder
folder_with_user_name.click()
time.sleep(2)

# Change to Share
driver.find_element(By.XPATH, '//*[@id="app-sidebar"]/ul/li[4]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="shareTabView"]/div/div/div/ul/li[2]').click()
time.sleep(2)

# Create a link to share the file
driver.find_element(By.XPATH, '//*[@id="shareDialogLinkList"]/div[2]/button').click()
time.sleep(2)

# Input the name of the link
driver.find_element(By.NAME, 'linkName').clear()
driver.find_element(By.NAME, 'linkName').send_keys('Acesso VPN USER')

#Define a password
driver.find_element(By.XPATH,'//*[@id="linkPassText-view23"]').send_keys('password')
time.sleep(10)

# Get the data of expiration of the file
expiration_date = driver.find_element(By.CLASS_NAME, "public-link-modal--input").get_attribute("value")
print(expiration_date)

# Button to create a link
driver.find_element(By.CLASS_NAME,'primary').click()
# Pause execution for 30 seconds
time.sleep(30)

# Close the browser


driver.quit()
