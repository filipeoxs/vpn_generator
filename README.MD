

O VPN Generator WebPy é uma aplicação web construída em Flask, Bootstrap e LDAP para simplificar a criação e gerenciamento de conexões VPN. Este projeto oferece uma interface intuitiva para os usuários gerarem, consultar a validade e realizar o download de VPNs de maneira fácil e segura.

# Recursos Principais
# Geração de VPN: 
Permite aos usuários criar novas VPNs especificando seu nome de usuário e selecionando o sistema operacional desejado (Windows, Mac OS, Android, Linux).
# Consulta de Validade: 
Oferece a capacidade de verificar a validade de uma VPN fornecendo o nome do usuário.
# Download de VPN: 
Possibilita o download de VPNs existentes, exigindo apenas a identificação do usuário.
# Tecnologias Utilizadas
* Flask: Framework web leve e flexível em Python. 
* Bootstrap: Framework front-end para uma interface responsiva e agradável. 
* LDAP3: Biblioteca Python para interação com servidores LDAP, utilizada para autenticação e busca de usuários no Active Directory.
* Selenium: Ferramenta de automação para testes web e scraping, integrada para realizar tarefas específicas.

# Instalação Local
* Clone o repositório: git clone https://github.com/filipeoxs/vpn_generato.git 
* Instale as dependências: pip install -r requirements.txt 
* Execute a aplicação: python app.py

## Ambiente Virtual

```markdown
## Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do projeto. Execute os seguintes comandos:

bash
python -m venv venv
source venv/bin/activate  # Linux
.\venv\Scripts\activate  # Windows

## Executando com Docker

Certifique-se de ter o Docker instalado. Em seguida, execute os seguintes comandos:

```bash
docker build -t vpn-generator-webpy .
docker run -p 5000:5000 vpn-generator-webpy


