# Importação da classe Flask do pacote flask
from flask import Flask

# Cria uma instância do aplicativo Flask chamada app
app = Flask(__name__)

# Define uma rota raiz para a aplicação e retorna a mensagem no navegador
@app.route('/')
def home():
    return "Olá, mundo! Esse é um app Flask."

# Iniicar servidor Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0')
