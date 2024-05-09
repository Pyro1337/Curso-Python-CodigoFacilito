#Se declara un diccionario vacio, a medida se va cargando y estos son separados mediante las comas ',' y remarcan su inicio
#y final mediante llaves {}
elementos = {}
elementos['nombre'] = 'Cody'
elementos['curso'] = 'Curso de Python'
print(elementos)
print(len(elementos))#saber la longitud del diccionario

#para actualizar las llaves es como el de agregar simplemente :
elementos['nombre'] = 'Ivan'
print(elementos)

#Otra forma de definir diccionarios es mediante : 
element = {'a' : 1 , 'b' : 2 , 'c' : 3 , 'a' : 4} #Se define su clave : valor
print(element)