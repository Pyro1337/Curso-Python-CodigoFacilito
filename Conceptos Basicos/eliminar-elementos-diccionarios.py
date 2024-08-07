diccionario = {'a':1, 'b':2, 'c':3, 'd':4}
print("Diccionario default",diccionario)
#Eliminamos mediante del nombreDiccionario['clave']
del diccionario['a']
print("Diccionario eliminado : ",diccionario)

#Otra forma de eliminar es mediante pop
diccionario.pop('b') #eliminamos mediante diccionario.pop('clave')
print(diccionario)

#Para eliminar todos los elementos del diccionario usamos diccionario.clear()
print(diccionario.clear())