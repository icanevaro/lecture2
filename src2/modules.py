#MODULOS#

#Los modulos sirven para importar cosas de otros archivos.
#En este caso una funcion. 
from functions import square

print(square(10))

#SI lo vemos por arriba diriamos que si ejecutamos esto nos va a traer 10*10 = 100
#Pero en realidad nos trae tambien el loop que habiamos definifo...
#Porque importe el archivo y decidio ejecutar todo. 

#Entonces si solo queremos la funcion y no el loop:
#Tengo que ir a functions.py y definir el loop como una funcion. 
# def main(): 
   #for.....

# Y tambien al final, en ese archivo (functions.py), tengo que agregar
# if __name__ == "__main__":
#       main()

#ahora cuando importemos la funcion del archivo, solo nos va a importar la funcion, y no el loop. 
