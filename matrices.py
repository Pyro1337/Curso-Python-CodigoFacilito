#Para crear matrices de n dimensiones se hara de la siguiente forma
#Suponiendo que sera uno de 2x2
columna_a = [10,20]
columna_b = [30,40]
#Para crear una matriz lo hacemos de la siguiente forma
matriz = [columna_a,columna_b]
print(matriz) #Esto me devuelve [[10, 20], [30, 40]] que seria columnaA columnaB
#Si queremos obtener el primer elemento de la matriz entonces lo hacemos con matriz[posicionX][posicionY]
print("El elemento 00 es ",(matriz[0][0]))