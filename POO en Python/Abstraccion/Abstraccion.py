from abc import ABC, abstractmethod

class Animal(ABC):  # Clase abstracta
    @abstractmethod
    def hacer_sonido(self):
        pass  # Este es un método abstracto que debe ser implementado por las clases hijas

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

# Ejemplo de uso
mi_perro = Perro()
mi_gato = Gato()

print(mi_perro.hacer_sonido())  # Salida: Guau
print(mi_gato.hacer_sonido())   # Salida: Miau


""""La abstraccion es un principio de la programación orientada a objetos que permite enfocarse en los aspectos escenciales de un objeto sin preocuparse por los detalles complejos de su implementación interna.
Básicamente la abstracción oculta detalles complejos y solo expone lo que es necesario para que se pueda ver algo.
Las clases abstractas no estan destinadas a ser instanciada directamente, una clase abstracta puede contener métodos abstractos, que son declarados pero sin implementarse, y las clases hijas
que heredan de una clase abstracta estan obligados a implementar estos métodos.*"""

