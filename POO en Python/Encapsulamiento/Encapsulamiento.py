#Encapsulamiento
#Como se mencionó con anterioridad en Python no se puede realizar encapsulamiento sin embargo la forma de hacer entender que queremos que dicho atributo sea privado
#es mediante la siguiente forma:
class MiClase:
    def __init__(self):
        self._atributo_privado = "Valor privado" #llamandolo _atributo_privado damos a entender que con ese guion bajo se llaman a los privados
        #para que otros desarrollores puedan comprenderlo.

#Si queremos acceder desde fuera en teoria no deberia mostrarnos pero aqui vemos que si igualmente un atributo privado puede ser llamado.
Objeto = MiClase()
print(Objeto._atributo_privado)

#Ahora si de verdad queremos que un atributo si o si sea muy privado lo haremos de la siguiente forma
class repriv:
    def __init__(self):
        self.__atributo_privado_2 = "Prueba atributo re-privado"



Objeto2 = repriv()
print(Objeto2.__atributo_privado2)
