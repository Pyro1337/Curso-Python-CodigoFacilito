
#Ahora mediante el uso de getters y setters se haria de esta forma.
class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age

    
    #Getter mediante @Property
    @property
    def nombre(self):
        return self._name
    
    #Setter mediante @NombreVariable.Setter
    @nombre.setter
    def nombre(self,nuevo_nombre):
        if isinstance(nuevo_nombre,str) and len(nuevo_nombre) > 0:
            self._name = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacia")
    
    #Getter mediante @Property
    @property
    def edad(self):
        return self._age
    
    #Setter mediante @NombreVariable.Setter
    @edad.setter
    def edad(self,nueva_edad):
        if isinstance(nueva_edad,int) and nueva_edad > 0:
            self._age = nueva_edad
        else:
            raise ValueError("La edad debe ser un entero mayor a 0")
    

P1 = Person("Ivan",21)
print("La edad es : "+str(P1.edad))
P1.edad = 23
print(P1.nombre)
print(P1.edad)

    


