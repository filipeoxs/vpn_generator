from flask import Flask, render_template, request
from ad_connection import start_search
import os
app = Flask(__name__)

# Main route for the app
@app.route('/', methods=['GET', 'POST'])
def index():
    resultado_busca=''
    if request.method == 'POST':
        # Pull the data from the html
        nome_usuario = request.form.get('nome_usuario')

        # Verify on AD
        resultado_busca = start_search(nome_usuario)
        try:
        
            if resultado_busca == nome_usuario:
                # Send the data to front end
                # Return the file of vpn
                file_vpn = 'Usuário encontrado'
                vpn = {'resultado_busca': file_vpn}
                return render_template('index.html', context=vpn)
            else:
                # Send error to html
                return render_template('index.html', error_msg=resultado_busca)
        except Exception as e:
            # Se a validação falhar, captura a exceção e renderiza a página de erro
            return render_template('index.html', error_msg=str(e))

    return render_template('index.html', context=resultado_busca)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
