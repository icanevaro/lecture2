
#TEMPLATES#

#Ahora queremos que flask tome archivos html que querramos utilizar. 
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
#la funcion podes llamarla como vos quieras, ya que la estas definiendo vos. 
def index():
    return render_template("index.html")
