lista = [1,2,3,4,5]

tupla = (10,20,30,40,50)

resultado = zip(tupla,lista) # -> Zip(iterable1,iterable2)

print(resultado) # ->Sale el zipeado
print(type(resultado))

#Se puede nuevamente convertir esto a una tupla
print(tuple(resultado)) #-> al convertir en una tupla se muestra ((iterable11,iterable21),(iterable12,iterable22),...)
#((10, 1), (20, 2), (30, 3), (40, 4), (50, 5))
print(type(tuple(resultado)))