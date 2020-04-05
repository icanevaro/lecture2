# es un colector de items donde esos items nunca aparecen dos veces.
#no importa el orden de los items
s = set()
s.add(1)
s.add(3)
s.add(5)
s.add(3)
print(s)

#items en el set son unicos. Si agrego un valor en el set que ya estaba, este valor no se va a repetir en el set si lo ejecuto
#Si ejecuto sets.py me va a devolver {1, 3, 5}

