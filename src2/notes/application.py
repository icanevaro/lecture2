#Las sesiones sirven para que para la misma pagina, pueda haber distintos usarios usando notas. y no puedan ver las notas del otro. 
#para eso vams a importar la parte de session de flask
from flask import Flask, render_template, request, session
#y aca estoy importando un modulo adicional de flask de sesiones
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#Defini esta variable notes, con luna lista vacia
notes = []

@app.route("/", methods=["GET", "POST"])
#Defino la funcion index;
def index():
#Esto la agrego para que  la lista este vacia, solo cuando no agregue nada a la lista todavia, para que no me rescriba cuando agrego otra nota   
    if session.get("notes") is None:
#Esto se agrega para decirle, que mi sesion tiene que tenes la lista de notas vacia.
        session["notes"] = []
#Entonces, si el rquest method es post, entonces agarra todo lo que sea note y agregalo a la lista de arriba.
    if request.method == "POST":
        note = request.form.get("note")
#agarra lista y agrega lo que esta introduciendo el usuario
       # notes.append(note)
#SI agrego esto, entonces solo se van a agregar las notas de mi sesion y no la de otros usuarios. 
        session["notes"].append(note)
#y recien ahi voy a ejecutar index.html y le paso todas esa notas. 
    return render_template("index.html", notes=session["notes"])

#Si reinicio el servidor pierdo las notas. Pero si cierro la pagina y la abro sin apagar el servidor, se guardan. 

#Despues de lo que se agrego, si apago el servidor y lo vuelvo a prender, me va a guardar las notas en la sesion. 
#Documentacion en pag de FLASK