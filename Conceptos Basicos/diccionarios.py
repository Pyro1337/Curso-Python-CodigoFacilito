#Los diccionarios nos permiten agregar o quitar elementos como una lista o tuplas, y son mutables es decir pueden ser
#modificados.

#Declaracion de un diccionario
diccionario = {} #una forma de declarar

diccionario = dict() #otra forma de hacerlo

#{llave: el valor al cual queremos asociar}
diccionario = { "total": 55} #para un solo valor dentro del diccionario
diccionario = {"total": 55 , "descuento": True, "subtotal": 15} #para varios pero de distintos tipos

#estos diccionarios pueden llegar a ser los equivalentes a un Json en Python

#Aqui declaramos este diccionario de usuario como un Json.
usuario = {
    'nombre': 'ivansanr_',
    'edad' : 22,
    'curso' : 'Curso de Python',
    'skills' : {
        'programacion' : True,
        'base_de_datos': False
    },
    'medallas' : ['Basico', 'intermedio']
}


#Agregar nueva llave valor al diccionario
diccionario ['usuario'] = 'ivansanr_'
#Editar una llave valor del diccionario
diccionario['usuario'] = 'ivansanr'
#Obtener el valor mediante una llave
print(diccionario['usuario']) # -> Devuelve ivansanr


#Se pueden obtener todas las llaves de un diccionario mediante keys.
print(usuario.keys()) #-> Nos devuelve dict_keys(['nombre', 'edad', 'curso', 'skills', 'medallas'])

#Se pueden obtener los valores de un diccionario mediante .values
print(usuario.values())

#Para imprimer las claves y valores juntas
for key, value in usuario.items():
    print(key, value)
#Esto devuelve lo siguiente
'''
nombre ivansanr_
edad 22
curso Curso de Python
skills {'programacion': True, 'base_de_datos': False}
medallas ['Basico', 'intermedio']'''

#Metodo Get, se obtiene el valor del diccionario mediante su llave, lo beneficioso es que con get
#si no encuentra un valor entonces se puede establecer uno por defecto.

user = {
    'name' : 'Ivan Sanchez',
    'age' : 22,
    'job' : 'Developer'
}

calificaciones = user.get('calificaciones,',[])
if calificaciones:
    for calificacion in calificaciones:
        print(calificacion)

