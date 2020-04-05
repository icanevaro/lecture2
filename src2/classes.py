#CLASSES#

#es para representar un punto en el espacio
#estoy definiendo una nueva calse de cosas llamada "Point"
class Point:
# El "init" sirve para decirle a python, despues de crear la clas, que es lo que necesito para esta  
#self es el objeto de la clase que recien cree y despues con x, y defino atributos para ese objeto. 
    def __init__(self, x, y):
#voy aguardar x e y en self. 
        self.x = x
        self.y = y
#Y aca lo llevo a la practica. Si imprimo p.x y p.y. se van a imprimir los dos valores que defini en point
p = Point(3, 5)
#Aca imprimo el valor x de mi point
print(p.x)
#Aca imprimo el valor y de mi punto
print(p.y)
