#URLS#

from flask import Flask, render_template

app = Flask(__name__)

#Ahora vamos a agregar una ruta que levante index.html
@app.route("/")
def index():
    return render_template("index.html")

#Y vamos a agregar otra ruta que levante more.html
@app.route("/more")
def more():
    return render_template("more.html")
