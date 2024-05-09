diccionario = {'a': 1 , 'b': 2, 'c': 3 , 'd': 4}
#keys
#values
#items
print(diccionario)
#Imprimir todas las llaves del diccionario
llaves = diccionario.keys()
print(llaves)
#Tambien podemos convertir esto a una lista de llaves
lista_llaves = list(diccionario.keys()) #->Convertimos a una lista con las llaves.
print(lista_llaves) #Retorna : ['a', 'b', 'c', 'd']

#Imprimir todos los valores del diccionario
valores = diccionario.values()
print(valores)
#tambien podemos convertir esto a una lista de valores
lista_valores = list(diccionario.values())
print(lista_valores)

#Para imprimir los items en total.
items = diccionario.items()
print(items)
#tambien se pueden convertir a una lista de items
lista_items = list(diccionario.items())
print(lista_items)