#Aca importe tambien un request. Es decir que lo que el usuario escriba se guardar en el server. 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

#Aca es donde le vamos a decir, que vamos a usar la info de index.html (method = ["POST"])
@app.route("/hello", methods=["GET","POST"])
#Si queremos ir directo a /hello, nos tira un error, porque el unio methodo que estaba aguantando el url era post
#ahora si queremos que soporte ir sirectamente a /hello, agregamos "GET" y despues agregamos la condicion a continuacion:
def hello():
#Creo la variable name, que me traiga lo que escriba el usuario en index.html
    if request.method == "GET":
        return "Please submit the form instead."
    else:    
        name = request.form.get("name")
#y aca le estoy diciendo que ejecute hello.html y defino la funcion name que es la que defini y la que voy a usar en la pagina hello.html
        return render_template("hello.html", name=name)
#el name= name sirve para poder luego, mostrarlo en la pagina de hello.html
