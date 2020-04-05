#DICCIONARIOS#
#Para establecer relaciones entre valores. 
#Quiero guardar las edades de cada persona.
#Alice en mi diccionario de edades y le digo que su valor va a ser 22. 

ages = {"Alice": 22, "Bob": 27}

#Si quiero agregar un valor despues de haber creado el diccionario:
ages["Charlie"] = 30

#Si quiero incrementar el valor de uno de mis datos en el diccionario:
ages["Alice"] += 1 #esto es un shortcut, en realidad se esribe: ages["Alice"] = ages["Aleice"] + 1

print(ages)

