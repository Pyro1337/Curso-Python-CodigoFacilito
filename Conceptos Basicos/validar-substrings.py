#El count nos puede servir para verificar cuantas veces se encuentra una porcion de cadena dentro de un String mas grande
#cadena.count("CadenaABuscar")
titulo_curso = 'Curso Profesional de Python, donde aprenderemos el uso de Python'
contador = titulo_curso.count('Python') #dentro del parentesis colocamos el string a buscar incluso puede ser un caracter
print(contador)
if contador >= 1 : #si encuentra almenos una coincidencia entonces imprimira el mensaje
    print("Python se encuentra en la cadena")
else:
    print("No se encontro la porcion de cadena en el String  general")

#otra forma es utilizando el in como vimos anteriormente este nos devuelve true o false.
print ('Python' in titulo_curso) #Si es True en este caso quiere decir que se encuenta en la cadena

#Uso del lower y Upper en Strings
print(titulo_curso.lower())
print(titulo_curso.upper())

#Startswith Endswith para saber si empieza o finaliza con, esto nos retorna true or false como es un metodo usa ()
print("El titulo inicia con C? ",titulo_curso.startswith('C'))
print("El titulo termina con Python",titulo_curso.endswith('Python'))

