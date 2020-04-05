from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

#/<string:name> cuando pponemos barra un nombre, la pagina va a decir autmaticamente "Hello, nombre"
@app.route("/<string:name>")
def hello(name):
#Si agregamos esta linea, le estamos diciendo que la primera letra del nombre sea mayuscula. 
    name = name.capitalize()
#Si le queremos agregar un poco de onda, podemos usar html
    return "<h1>Hello, {}!<h1>".format(name)
