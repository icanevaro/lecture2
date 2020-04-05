from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
#Genero una variable que contiene una lista de nombres
#Si luego de haberlo corrido agrego un nombre a la lista, el loop lo va a tomar automaticamente
    names = ["Alice", "Bob", "Charlie", "David"]
    return render_template("index.html", names=names)
