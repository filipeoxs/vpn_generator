# Import necessary modules from Selenium and other libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from read_configs import read_configs

# Get URLs from the configuration file
urls = read_configs()
urlvpn1 = f'http://{urls[2]}'

# Pause execution for 10 seconds
time.sleep(10)

# Get the second URL from the configuration file
urlvpn2 = f'http://{urls[3]}'

# Configure Chrome options to disable SSL certificate verification
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

# Additional capabilities to accept insecure certificates
capabilities = {
    'acceptInsecureCerts': True
}

# Initialize the Chrome browser with configured options and capabilities
browser = webdriver.Chrome(options=chrome_options, capabilities=capabilities)

# Navigate to the first URL
browser.get(urlvpn1)

# Perform necessary operations...

# Close the browser
browser.quit()
