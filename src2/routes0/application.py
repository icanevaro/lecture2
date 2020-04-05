from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

#agregamos otra ruta al ambiente. Entonces si yo ejecuto flask, me va a llevar a la pagina que dice Hello World, pero si le agrego "/david" al url, me va a llevar a lo que haya definido abajo: 
@app.route("/david")
def david():
    return "Hello, David!"

@app.route("/maria")
def maria():
    return "Hello, Maria!"

