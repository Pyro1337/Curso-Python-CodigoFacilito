#Primeramente crearemos una lista numerica
lista = [1, 90, 35, 132, 3400, 0 , -5, 3]
print("La lista  principal es : ",lista)
#Ordenamiento de listas si todas las listas son de un mismo tipo de dato.
#Utilizaremos la funcion SORT para ordenar las listas, es una palabra reservada de Python que hace el ordenamiento ascendentemente.
lista.sort()
print("La lista ordenada ascendente es ",lista)
#Ordenamiento descendente mediante sort con parametro nombreLista.sort(reverse=True)
lista.sort(reverse=True)
print("La lista ordenada descendentemente es : ",lista)

#Para obtener el menor numero y el mayor numero dentro de un listado
lista.sort()#ordenamos ascendentemente
print("La lista ordenada es : ",lista)
print("El menor elemento es : ",lista[0])#Nos devuelve el menor valor
print("El mayor elemento es : ",lista[-1])#Nos devuelve el mayor en este caso el de la ultima posicion que se consigue con -1

#Otra forma de obtener el menor es mediante min(lista), y el mayor es con max(lista) sin necesidad de ordenar.
print("El menor elemento de la lista es ",min(lista))
print("El mayor elemento de la lista es ",max(lista))

#Como verificar si un elemento se encuentra en la lista. utilizamos la palabra reservada in
# 0 in lista -> es como consultar 0 se encuentra en la lista? , devuelve True o False
#Tambien se puede verificar si no esta con el not in : 300 not in lista
print("La lista es : ",lista)
print("Se encuentra el 0 en la lista? : ",0 in lista)
print("El 300 no se encuentra en la  lista? ",300 not in lista)