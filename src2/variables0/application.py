
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
#Agregue una variable, llamada headline, que contiene el texto "Hello, world!"
    headline = "Hello!"
#Y aca le estoy diciendo que ademas de ejecutar index.html, que en el headline ponga lo que sea que haya puesto en la variable headline.
    return render_template("index.html", headline=headline)

#Use el mismo template de index.html, pero cambie la variable "headline" para que cambie el titulo a "Goodbye" en otra ruta
#Este codigo en python es codigo que se puede considerar "Back end code"
@app.route("/bye")
def bye():
    headline = "Goodbye!"
    return render_template("index.html", headline=headline)
