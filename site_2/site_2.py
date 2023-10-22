from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h2>Primeira página!</h2>"

@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome="mundo"):
    return "Olá, " + nome + "!"

if __name__ == '__main__':
    app.run(debug=True)

