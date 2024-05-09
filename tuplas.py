# Las tuplas permiten almacenar diferentes tipos de datos, digamos que serían como los Structs.
# Las tuplas son inmutables, una vez se define de una forma, así se queda por el resto del programa y no se pueden modificar los elementos.
# Las tuplas quedan así de manera permanente.
# Por ejemplo, supongamos que queremos colocar en la tupla 10 strings.
# Se usa paréntesis en vez de corchetes.

#           0     1  2     3
tupla = ('Prueba',2,True,[3,4,5])
print(type(tupla))  # Nos devuelve tipo tuple.
print(tupla)
print(len(tupla))
