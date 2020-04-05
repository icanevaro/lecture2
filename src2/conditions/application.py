#Importamos el modulo datetime que me va traer fechas
import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
#devino una variable que se llame now que me traiga el dia de hoy
    now = datetime.datetime.now()
#y despues defino una variable buleana que se llame new year. Va a ser true si es new year y va a ser fasle si no es new year
#Si no.month ==1 y now.day == 1 quiere decir que es new year. Osea que es el 01/01
    new_year = now.month == 1 and now.day == 1
#por ultimo, hago el render de index.html y le digo que la valor new_year (la que voy a poner en index.html) = la variable new_year(la que defini aca)
    return render_template("index.html", new_year=new_year)
