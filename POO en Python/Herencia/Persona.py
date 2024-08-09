class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("La persona esta hablando")

class Empleado(Persona): #-> De esta manera decimos que empleado es hijo de la clase padre Persona
    #Empleado tomara los mismos atributos de Persona pues lo heredamos.
    def trabajar(self):
        print("El empleado esta trabajando")
    

#Se asignan los valores para E1 -> Correspondiente a Empleado
E1 = Empleado("Ivan",27,"paraguayo")
print(E1.nombre+"\n"+str(E1.edad)+"\n"+E1.nacionalidad)
#Se llaman a las funciones, una es de la clase padre Personas la otra de la clase hija Empleado
E1.hablar()
E1.trabajar()    