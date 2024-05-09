lista = [8,90,30,300,3450,212,500,1000]
#Supongamos que buscamos un numero si es que se encuentra en la lista pero queremos rescatar su indice, por lo que haremos lo siguiente
print("Se encuentra 300 en la lista? ",300 in lista)

indice_busqueda = lista.index(300) #nombre_lista.index("elemento a buscar")
print("El indice de 300 en la lista es : ",indice_busqueda)
#OBS: en caso que exista mas de un elemento repetido en busqueda unicamente retornara el primero que encuentre.