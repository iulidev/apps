"""
Executia aplicatie se realizeaza cu
python app.py

daca numele aplicatiei este diferit de app.py sau wsgi.py aplicatia se porneste
cu python app.py direct dar pentru a executa cu "flask run" realizam in
prealabil exportarea/setarea unei variabile de environment care sa
specifice numele aplicatiei (__name__ - numele modulului, al scriptului)

flask run
    este o alternativa pentru a porni serverul si a face aplicatia
    accesibila in browser, actualizarea aplicatiei este realizata dupa
    restartarea web server-ului

debug=True  permite actualizarea aplicatiei fara a fi nevoie de repornirea
            serverului
Configuratia aplicatiei flask:
https://flask.palletsprojects.com/en/2.0.x/config/
In cmd Windows schimbam contextul din production in development:
(default/implicit environment este "production")
set FLASK_ENV=development

In powershell
$env:FLASK_ENV = "development"
Alternativ, se poate seta contextul cu atributul config, care este un dictionar
app.config['ENV'] = "development"

Web serverul WSGI intern, implementat cu Werkzeug, este pentru mediu de test
Command line interface:
https://flask.palletsprojects.com/en/2.0.x/cli/?highlight=flask_app

Adaugarea de variabile in URLs
https://flask.palletsprojects.com/en/2.0.x/quickstart/?highlight=route%20parameters

Jinja templating engine:
https://jinja.palletsprojects.com/en/3.0.x/
https://jinja.palletsprojects.com/en/3.0.x/templates/

"""
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
app.config['ENV'] = "development"

web_frameworks = ["Flask", "Django", "Plone"]


@app.route('/')
def home():
    return render_template("index.html", title="Home", entries=web_frameworks)


@app.route('/about')
def about():
    return render_template("about.html", title="About")


@app.route('/users/<string:name>')
def users(name):
    return f"Salut {name}!"


@app.route('/despre')
def despre():
    return redirect(url_for("about"))


@app.route('/students/<student>')
def students(student):
    return redirect(url_for("users", name=student))


if __name__ == '__main__':
    app.run(debug=True, port=7007)
