'''Metodo Split : Permite generar una lista a partir de un String
se le aplica la funcion cadena.split() -> cada posicion
estara determinada por el espacio dato1 dato2 entonces seria posicion 0 y 1 respectivamente.'''
lenguajes = 'Python Ruby Java Rust C++ C C#'
listado_lenguajes = lenguajes.split() 
print(listado_lenguajes) #-> quedaria : ['Python', 'Ruby', 'Java', 'Rust', 'C++', 'C', 'C#']
print(len(listado_lenguajes)) #la longitud es 7

#Que pasaria si el string esta separado por guiones?
#cadena.split('divisor-de-cadena') ej: cadena.split('-') estoy diciendo que separe siempre que encuentre guiones.
language = 'Python-Ruby-Csharp-C++-Perl-Php'
list_language = language.split('-')
print(list_language) #-> el resultado es ['Python', 'Ruby', 'Csharp', 'C++', 'Perl', 'Php'] pues separo al encontrar -
print(len(list_language))

'''Metodo Join
Es el opuesto pues este permite crear cadenas a partir de listas'''
# cadena = 'separador'.join(lengua) lo normal es separar por espacios cadena = ' '.join(lista)
lengua = ['Python','Java','Ruby','Perl']
string_lengua = ' '.join(lengua)
print(string_lengua)
print(type(string_lengua))
#Supongamos que queremos separarlos por ; entonces
string_lengua2 = ';'.join(lengua)
print(string_lengua2)
print(type(string_lengua2))
