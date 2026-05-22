from flask import Flask


app = Flask(__name__) # inicio o flask

@app.route('/') # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def ola_mundo():
    return 'Olá, Mundo!' # Isso é o que será retornado quando a rota '/' for acessada

@app.route('/hello') # Isso é outro decorator, mapeando a função abaixo para a rota '/hello'
def hello():
    return 'Hello, World!' # Isso é o que será retornado quando a rota '/hello' for acessada

@app.route('/decorator')
def sadudacao():
  return 'O que é um decorator em Python: Um decorator em Python é uma função que modifica ou estende o comportamento de outra função, método ou classe sem alterar seu código-fonte original. <br> ' \
  'Decorators servem para modificar ou estender o comportamento de funções ou métodos sem alterar seu código-fonte original. <br>' \
  'No Flask, o decorator @app.route é utilizado para vincular uma URL específica a uma função Python, mapeando endereços da web para lógica de backend. '

if __name__ == '__main__':
    app.run(debug=True) # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento
