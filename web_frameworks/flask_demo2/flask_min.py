# Flask app quickstart (tutorial, documentatie oficiala)
# https://flask.palletsprojects.com/en/2.0.x/quickstart/
# Cand pornim serverul pentru a testa aplicatia cu "flask run"
# daca numele este diferit de app.py sau wsgi.py trebuie
# exportat numele scriptului intr-o variabila de mediu

# in PowerShell se exporta numele fisierului intr-o var
# $env:FLASK_APP = "flask_min"
# in command prompt Windows 
# set FLASK_APP=flask_min

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Home page second app"


@app.route('/about')
def about():
    return "About page. O alta aplicatie web simpla in Flask 2.0"


if __name__ == '__main__':
    app.run(debug=True)
