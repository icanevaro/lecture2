#FLASK#


#Importamos flask (despues de descargarlo)
from flask import Flask
#Le damos el entorno de app
app = Flask(__name__)
#le indicamos la ruta
@app.route("/")
#Definimos una variable que retorne algo
def index():
    return "Hello, world!"
