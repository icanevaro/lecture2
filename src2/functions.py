#FUNCIONES#

#Defino una funcion propia, con un argumento que va a ser "x"
def square(x):
    #Si vos me pedis "x" te voy a devolver x*x
    return x * x
#Voy definir la funcion para cuando lo quiera importar en otro archivo no me traiga esto tambien
def main():
#Y aca voy a utilizar la funcion que arme, para hacer un loop y decir: el numero que ponga al cuadrado es igual a ...     
#Uso un .format para definir que va entre {}.
    for i in range(10):
        print("{} squared is {}".format(i, square(i)))
#lo que me va a mostrar es: de 0 a 9 ese texto que estoy definiendo, con el resultado automatico
#Pregunta:Tengo que definir la funcion antes de usarla?
#Si, tengo que definirla antes, excepto que ya exista. Tiene que estar antes del for la funcion. 
#Python lee de arriba para abajo. 
#Hay un work around. 
#Podemos usar funciones que escribiste en otro archivo. 

#Y tengo que agregar algo mas para que no se ejecute cuando lo importo
#agrego, si name igual main, si estoy corriendo este archivo, corre la main function
if __name__ == "__main__":
    main()