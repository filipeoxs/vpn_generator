from flask import Flask, render_template, request
from ad_connection import start_search
import os
from vpn_gen import search_certificate, download_vpn, login

app = Flask(__name__, static_folder='static')

# Main route for the app
@app.route('/')
def index():
    return render_template('index.html')

# Função para realizar a busca de usuário
@app.route('/search_user', methods=['POST'])
def search_user():
    if request.method == 'POST':
        # Recupera o nome do usuário
        nome_usuario = request.form.get('nome_usuario')
        try:
            # Verifica se existe esse usuário no AD
            resultado_busca_ad = start_search(nome_usuario)
            
            # Se existir, busca no pfSense o certificado
            if resultado_busca_ad == nome_usuario:
                # Inicia a busca no pfSense
                certificado_pfsense = search_certificate(nome_usuario)
                # Retorna os dados do pfSense
                vpn = {'resultado_busca': certificado_pfsense, 'nome_usuario': nome_usuario}
                return render_template('index.html', context=vpn)
            else:
                # Retorna informando que o usuário não foi encontrado do AD
                return render_template('index.html', error_msg=resultado_busca_ad)
        except Exception as e:
            return render_template('index.html', error_msg=str(e))
        

# Função para realizar o donwload de um certificado 
@app.route('/download_certificado', methods=['POST'])
def download_certificado():
    if request.method == 'POST':
      nome_de_usario = request.form.get('nome_usuario')
      try:
            # Verifica se usuario existe no AD
            busca_ad_usuario = start_search(nome_de_usario)
            # Se existir, busca no pfSense o certificado
            if busca_ad_usuario == nome_de_usario:
                # Inicia a busca no pfSense
                certificado_pfsense = download_vpn(nome_de_usario)
                return render_template('index.html')
            else:
                # Retorna informando que o usuário não foi encontrado do AD
                return render_template('index.html', error_msg=busca_ad_usuario)
      except:
          pass


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
    
    
