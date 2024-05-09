calificacion = 10
color = None
if calificacion >= 7 :
    color = 'Verde'
else:
    color = 'Rojo'
print("La calificacion es : ",calificacion," el color es : ",color)


#Para evitar estas lineas de codigo, utilizaremos el operador ternario en python. de la siguiente forma
color = 'Verde' if calificacion >= 7 else 'Rojo' #Variable afectada, condicion , lo que pasa sino se cumple la cond
print(calificacion,color)