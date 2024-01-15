from flask import Flask, render_template, request
from ad_connection import start_search
app = Flask(__name__)

# Main route for the app
@app.route('/', methods=['GET', 'POST'])
def index():
    resultado_busca = ""
    if request.method == 'POST':
        # Pull the data from the html
        nome_usuario = request.form.get('nome_usuario')

        # Verify on AD
        resultado_busca = start_search(nome_usuario)
        
        print (nome_usuario)
        
        # Send the data to front end
        context = {'resultado_busca': resultado_busca}
        return render_template('index.html', context=context)

    return render_template('index.html', context=resultado_busca)

if __name__ == '__main__':
    app.run(debug=True)
