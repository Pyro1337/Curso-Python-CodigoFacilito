cursos = ['Python', 'Django', 'Flask']

cursos_tupla = tuple(cursos) #Convierte de una lista a tupla

print("Cursos en lista : ",cursos)
print(type(cursos))
print("Cursos en tuplas : ",cursos_tupla)
print(type(cursos_tupla))

cursos_tupla_a_lista = list(cursos_tupla) #Convierte de tupla a lista
print("De tuplas a lista es : ",cursos_tupla_a_lista)
print(type(cursos_tupla_a_lista))