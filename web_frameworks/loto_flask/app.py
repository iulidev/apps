"""
Aplicatie web loto 6/49
"""

from flask import Flask, render_template
import random


lista = list(range(1, 50))

random.shuffle(lista)
numere_extrase = [lista.pop() for i in range(0, 6)]

app = Flask(__name__)

app.config['ENV'] = "development"


@app.route('/')
def index():
    return render_template("index.html", title="Loterie")


@app.route('/loto')
def loto():
    return render_template("loto.html", numere=numere_extrase, title="Numere loto")


if __name__ == '__main__':
    app.run(debug=True, port=7000)
