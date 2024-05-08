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