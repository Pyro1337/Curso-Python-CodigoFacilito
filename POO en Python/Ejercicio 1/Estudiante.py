#Crear una clase Estudiante, que tenga atributos tales como Nombre,Edad,Grado
#Que contenga el método estudiar(), e imprima el nombre y posteriormente, esta estudiando
#Se debe pedir todos los datos : Nombre Edad y Grado.
class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    #Funcion estudiar.
    def estudiar(self,nombre,edad,grado):
        print("El estudiante " +nombre+ " esta estudiando tiene " +str(edad)+ " anios y esta en el " +str(grado) +" grado")
    
    
nombre = input("Ingrese el nombre del estudiante: ")
edad = input("Ingrese la edad: ")
edad = int(edad)
grado = input("Ingrese el grado : ")
grado = int(grado)

e1 = Estudiante(nombre,edad,grado)
e1.estudiar(nombre,edad,grado)

        