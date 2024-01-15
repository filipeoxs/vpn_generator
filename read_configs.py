import configparser

# Store the username and the password from the file conf
def read_configs():
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Read the .ini file
    config.read('config_dev.ini')

    # Access the values using the appropriate section and key
    username = config.get('Credentials', 'username')
    password = config.get('Credentials', 'password')
    url_bsb = config.get('vpn', 'url_bsb')
    url_rj = config.get('vpn', 'url_rj')

    return username,password, url_bsb, url_rj