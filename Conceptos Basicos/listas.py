#Para creacion de listas podemos usamos list() o mediante corchetes de la siguiente forma:
lista = ['String', 10 , 10.5 , True] #Este list puede contener todo tipo de dato y quedaria tal que asi
print (lista)
#A cada valor de la lista, le corresponde un indice, el String le corresponde 0
lista_strings = ["Ivan" , "Curso", "Python"]

lista_enteros = [-10, 10 ,0 , 300]

lista_floats = [10.5 , -20.5 , 30.5 , 100.00]

lista_booleanos = [True , True, False , (2>10), (2<=10), (4 > 3 and 10 != 11)]
#                0           1        2       3       4
lista_cursos = ['Python', 'Django', 'Flask', 'Java', 'Ruby']
#                1          2         3        4       5
primer_curso = lista_cursos[3]
print("El curso en la 4ta posicion es : ",primer_curso)

#si se realizan busquedas en una lista con una posicion que sobrepasa la cantidad entonces saca un out of range.


#Si se desea actualizar una posicion podemos hacerlo por las posiciones
lista_cursos [4] = "Rust"
print("El nuevo curso editado es : ",lista_cursos[4])

#Creacion de sublistas.
#sublista_ lista_nueva[inicial:final]
#contempla el inicial pero es entre el final NO el FINAL
sub_lista = lista_cursos[0:3] #Aqui indicamos que vamos a tomar desde la posicion 0 hasta las 2 pues el 0-3 indica
#que se va tomar entre la 0 y las 
print(sub_lista) #Se imprime Python, Django Flask

#[start:end]
#[start:] -> Obtenemos los ultimos elementos de la lista
#[:end] -> Obtenemos los primeros elementos de la lista
#[start:end:skip] -> El skip serian los SALTOS que hara.


#Agregar elementos a la lista
lista_cursos.append('MongoDB') #Para agregar un elemento a la lista basta con utilizar append.
print(lista_cursos)

#Reemplazar el valor y mover la lista una posicion hacia la derechaa actualmente tenemos hasta :
#['Python', 'Django', 'Flask', 'Java', 'Rust', 'MongoDB'] entonces si realizo un lista_cursos.insert(0,'Pygame')
#entonces colocaria a Python en la posicion 1 y la 0 corresponderia ahora a Pygame
lista_cursos.insert(0,'Pygame')
print(lista_cursos) #nos devuelve ['Pygame', 'Python', 'Django', 'Flask', 'Java', 'Rust', 'MongoDB']
lista_cursos.insert(1,'PHP')
print(lista_cursos) # esto nos debe devolver ['Pygame', ,'PHP','Python', 'Django', 'Flask', 'Java', 'Rust', 'MongoDB']

#Longitud de una lista len(nombre_lista)
print("La longitud de la lista es de: ",len(lista_cursos)," cursos.")

#Para acoplar una lista pequeña a otra mas grande procederemos a crear un lista_cursos_2 agregaremos  algunos datos
#y posteriormente utilizaremos  la funcion extend para acoplar esa lista  mas chica a la principal desde su final.
lista_cursos_2 = ['C','C++','C#','Docker','GIT']
#Procedemos a acoplar la segunda lista a la primera : lista1.extend(lista2)
lista_cursos.extend(lista_cursos_2)
print("La lista acoplada es : ",lista_cursos) #nos devuelve ['Pygame', 'PHP', 'Python', 'Django', 'Flask', 'Java', 'Rust', 'MongoDB', 'C', 'C++', 'C#', 'Docker', 'GIT']

#Eliminar elementos de la lista por su contenido
#Supongamos que queremos eliminar Docker de la lista_cursos_2 utilizamos el metodo .remove('NombreElemento')
lista_cursos_2.remove('Docker')
print("La lista luego de eliminar Docker es : ",lista_cursos_2)

#Eliminar elementos de la lista por su posicion
#En este caso utilizaremos la  palabra reservada del nombre_lista[posicion]
#Supongamos que actualmente tenemos en lista_cursos_2 : ['C', 'C++', 'C#', 'GIT']
#Eliminemos la posicion 2 que corresponde a C#
del lista_cursos_2[2]
print("El resultado de eliminar la segunda posicion de la lista_cursos_2 es : ",lista_cursos_2)

#Eliminar todos los elementos de la lista
#Utilizamos el metodo clear lista.clear()
lista_cursos_2.clear()
print("La lista cursos 2 limpia es : ",lista_cursos_2," cuya longitud es ",len(lista_cursos_2))