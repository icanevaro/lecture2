#INHERITANCE#

#Este archivo va a ser igual al de urls, pero ahora vamos a querer hacer un .html base, para no tener que hacer dos archivos muy similares
#Y a partir de ese archivo base vamos a rellenar lo que falte para las diferencias de cada uno de los archivos (index y more)

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/more")
def more():
    return render_template("more.html")
