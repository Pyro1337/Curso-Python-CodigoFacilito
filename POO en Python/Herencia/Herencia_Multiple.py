#Creamos la clase Persona que sera la clase padre de todos los demas.
class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def Presentarse():
        print("Hola soy una persona")

#Clase empleado donde se agrega el salario
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad,salario):
        super().__init__(nombre, edad, nacionalidad)#se definen los atributos de la clase padre
        self.salario = salario
    
    def Trabajar():
        print("Se pone a trabajar...")

#Definimos la clase Programador el cual tiene un atributo lenguajes y una funcion programar.  
class Programador():
    def __init__(self,lenguajes):
        self.lenguajes = lenguajes
    
    def Programar():
        print("Se pone a programar...")

#Finalmente la clase desarrollador que hereda de empleado(que tiene atributos de Persona) y de Programador que es el de lenguajes
#Tambien tiene su propio atributo que es nivel y su funcion info_desarrollador que se usa para imprimir los resultados.    
class Desarrollador(Empleado,Programador):
    def __init__(self, nombre, edad, nacionalidad, salario,lenguajes,nivel):
        Empleado.__init__(self,nombre,edad,nacionalidad,salario)
        Programador.__init__(self,lenguajes)
        self.nivel = nivel
    #Se utiliza self como parametro pues todo lo que imprimeros esta contenido en el objeto
    def info_desarrollador(self):
        print(f"El dev {self.nombre}, cuya edad es {self.edad} y nacionalidad {self.nacionalidad} tiene un salario de {self.salario} y sabe los lenguajes {self.lenguajes} con nivel {self.nivel}")


#Para la carga de lenguajes usamos una lista primeramente vacía
lenguajes = []
while True:
    lenguaje = input("Ingrese el lenguaje, al finalizar envie X ")
    if lenguaje == "X": #Si se ingresa una X se corta el input
        break
    lenguajes.append(lenguaje) #Se añade si cumple que es distinto a X

dev = Desarrollador("Ivan",27,"Paraguayo",3500000,lenguajes,"Senior") #Creamos el objeto dev en base a Desarrollador y le pasamos los parametros
dev.info_desarrollador() #Llamamos a la función que imprime los resultados.

