from ldap3 import Server, Connection, ALL
import time
import logging
from read_configs import read_configs

configs = read_configs()

class AD:
    def __init__(self):
        self.conn = None
    # Connector do Active Directory
    def connect(self):
        try:
            while self.conn is None:
                # Define the username and password
                username = configs[0]
                password = configs[1]
                print(username)
                print(password)
                # Make connection with the server
                server = Server('ldap://10.1.1.19', get_info=ALL)
                self.conn = Connection(server, user=username, password=password)
               # If the username or the password does not match
                if not self.conn.bind():
                    logging.error(f'Erro de autenticação: {self.conn.result}')
                    self.conn = None
                    time.sleep(5)
                    return False
                else:
                    return True
            return True
         # if the connection does not work, show this message error
        except Exception as error_conn_ad:
            logging.error(f'Houve um erro na conexão LDAP.\nError: {error_conn_ad}')
            self.conn = None
            time.sleep(5)
            return False
    # Search for the user on AD to compare the user from ad and the user that was collected from frontend
    def search_user_samaccountname(self, display_name):
        if self.connect():
            self.conn.search('dc=ipea,dc=gov,dc=br', f'(sAMAccountName={display_name})', attributes=['sAMAccountName'])
            entries = self.conn.entries

            if not entries:
                return 'Usuário não encontrado no AD'
            else:
                return True
        else:
            return False

# start the class AD (Test)
def start_search(usuario_localizar_ad):
    ad_instance = AD()
    display_name_to_search = usuario_localizar_ad  # Substitua com o nome completo do usuário que você deseja pesquisar
    result = ad_instance.search_user_samaccountname(display_name_to_search)
    print(result)