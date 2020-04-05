#FLASK#


#Importamos flask (despues de descargarlo)
from flask import Flask
#Asignamos una variable  con el nombre "app", para luego poder hacer acciones con ella
app = Flask(__name__)
#le indicamos la ruta. Es decir, cuando alguien vaya a la ruta que utilize el ambiente, se ejecuta lo siguiente:
@app.route("/")
#Definimos una variable que retorne algo
def index():
    return "Hello, world!"
