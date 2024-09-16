#do modulo app, está sendo importado a variável app
from flask import render_template
from app import app

@app.route("/index/<usuario>")
#decorator, serve para aplicar uma função em cima de outra
#o método route define uma rota para essa página
@app.route("/", defaults={"usuario": None})
def index(usuario):
    return render_template('index.html', usuario= usuario)

"""
@app.route("/test/", methods=['GET'])
def test():
    return "Oi!"
"""