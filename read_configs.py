import configparser

# Store the username and the password from the file conf
def read_configs():
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Read the .ini file
    config.read('config.ini')

    # Access the values using the appropriate section and key
    username = config.get('Credentials', 'username')
    password = config.get('Credentials', 'password')
    

    return username,password