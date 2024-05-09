diccionario = {'a': 1, 'b': 2 , 'c': 3 }
valor = diccionario['c'] # se carga en la variable valor = diccionario['Clave']
print (valor) #-> sin embargo si no existe dicha clave lanzara un error en ejecucion KeyError.

#Podemos usar el in simplemente para verificar si se encuentra la llave dentro del diccionario
print ("Se encuentra a en el diccionario? ",'a' in diccionario)

#Uso del get, que recibe como argumento la llave del valor que queremos conocer.
valor2 = diccionario.get('x') #-> en este caso por mas que no exista no lanzara KeyError pues simplemente tirara none
print(valor2)
#Como devolver un mensaje por default si no encuentra nada
valor2 = diccionario.get('x', 'La llave no existe en el diccionario')
print(valor2)

#El metodo setDefault sino encuentra la llave entonces lanza un valor por defecto para el mismo.
valor2 = diccionario.setdefault('x','999') #-> Lanza por default 999 si no encuentra X
print(valor2)