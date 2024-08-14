class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("La persona está hablando")

class Empleado(Persona): 
    def trabajar(self):
        print("El empleado está trabajando")

# Se asignan los valores para E1 -> Correspondiente a Empleado
E1 = Empleado("Ivan", 27, "paraguayo")
print(E1.nombre + "\n" + str(E1.edad) + "\n" + E1.nacionalidad)
# Se llaman a las funciones, una es de la clase padre Persona, la otra de la clase hija Empleado
E1.hablar()
E1.trabajar()

# Herencia entre Persona y Desarrollador, con nuevos atributos para Desarrollador
class Desarrollador(Persona):
    def __init__(self, nombre, edad, nacionalidad, salario, nivel, lenguajes):
        super().__init__(nombre, edad, nacionalidad)
        self.salario = salario
        self.nivel = nivel
        self.lenguajes = lenguajes

    def programacion(self):
        #Aqui se hace un selfPrint utilizando self.Variables que ya se contienen.
        print(f"El dev {self.nombre}, cuyo nivel es {self.nivel}, se encuentra programando en el lenguaje {self.lenguajes}")
            

# Main
nombre = input("Ingrese el nombre del desarrollador: ")
edad = int(input("Ingrese la edad del Dev: "))
salario = float(input("Ingrese el salario en $: "))
nacionalidad = input("Ingrese la nacionalidad del Dev: ")
nivel = input("¿Qué nivel de desarrollo posee? : ")
lenguajes = []  # Creamos una lista vacía primeramente

while True:
    lenguaje = input("Ingrese el lenguaje que maneja, una vez finalizado presione X: ")
    if lenguaje.lower() == 'x':
        break
    lenguajes.append(lenguaje)

dev1 = Desarrollador(nombre, edad, nacionalidad, salario, nivel, lenguajes)
dev1.programacion()
dev1.hablar()