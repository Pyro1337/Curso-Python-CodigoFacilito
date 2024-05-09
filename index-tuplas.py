cursos = ('Python','Flask','Django','Rails','MongoDB')
#             0       1       2         3        4
primer_curso = cursos[2] #se puede guardar en una variable si se extrae por posicion
print(primer_curso)

ultimo_curso = cursos[-1] #se extrae el ultimo curso
print(ultimo_curso) 

#Se pueden generar subtuplas tal que asi
subtuplas = cursos[0:3:1] #Extrae [indice-inicial:entre-final:saltos]
print(subtuplas)
