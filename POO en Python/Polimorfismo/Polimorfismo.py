print("Metodo por herencia")
class Animal:
    def sonido(self):
        return "Sonido Animal"

class Gato(Animal):
    def sonido(self):
        return "Miau"

class Perro(Animal):
    def sonido(self):
        return "Guau"


G = Gato()
print(G.sonido())
P = Perro()
print(P.sonido())
A = Animal()
print(A.sonido())


#Polimorfismo mediante Duck Typing
#Si suena y camina como un pato entonces probablemente sea un pato.

print("\nMetodo Duck Typing")
#Declaramos la clase Perro
class Perro:
    def hacer_sonido(self):
        return "Ladrido"
#Declaramos la clase Gato
class Gato:
    def hacer_sonido(self):
        return "Maullido"
#Declaramos la clase Pato
class Pato:
    def hacer_sonido(self):
        return "Cuac"
#Finalmente en el Main definimos una funcion que lleva como parametro Animal e imprime parametro.hacer_sonido()
#Tener en cuenta que hacer_sonido es la funcion de las clases que quieren implementar este polimorfismo.
def reproducir_sonido(animal): 
    print(animal.hacer_sonido())

perro = Perro()
gato = Gato()
pato = Pato()

reproducir_sonido(perro)  # Salida: Ladrido
reproducir_sonido(gato)   # Salida: Maullido
reproducir_sonido(pato)   # Salida: Cuac
