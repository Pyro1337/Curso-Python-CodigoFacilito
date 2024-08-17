# Métodos Dunder o Especiales en Python
# Son métodos que empiezan y terminan con __ (dos guiones bajos)
# Estos métodos permiten sobrecargar operadores y modificar el comportamiento predeterminado de las clases.

class Persona:
    # __init__ es el constructor de la clase, se llama automáticamente cuando se crea una instancia.
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo privado (convención de guion bajo)
        self._edad = edad      # Atributo privado (convención de guion bajo)

    # @property: Define un getter para el atributo 'nombre'
    # Esto permite acceder a 'nombre' como si fuera un atributo, no un método.
    @property
    def nombre(self):
        return self._nombre

    # @nombre.setter: Define un setter para el atributo 'nombre'
    # Esto permite modificar el atributo 'nombre' de manera controlada
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacía")

    # Getter para el atributo 'edad' usando @property
    @property
    def edad(self):
        return self._edad

    # Setter para el atributo 'edad' usando @edad.setter
    # Controla que la edad sea un número entero positivo
    @edad.setter
    def edad(self, nueva_edad):
        if isinstance(nueva_edad, int) and nueva_edad > 0:
            self._edad = nueva_edad
        else:
            raise ValueError("La edad debe ser un entero positivo")

    # __str__: Define la representación en cadena del objeto para que sea legible cuando uses print()
    # Es equivalente a toString() en otros lenguajes como Java.
    def __str__(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}"

    # __repr__: Define la representación "oficial" del objeto, útil para depuración
    # Se usa cuando llamas a repr() o en entornos interactivos
    def __repr__(self):
        return f'Persona(nombre={self._nombre!r}, edad={self._edad!r})'

    # __eq__: Sobrecarga el operador == para comparar dos objetos Persona por nombre y edad
    def __eq__(self, otra_persona):
        return self._nombre == otra_persona.nombre and self._edad == otra_persona.edad

    # __add__: Sobrecarga el operador + para sumar las edades de dos objetos Persona
    def __add__(self, otra_persona):
        return self._edad + otra_persona.edad

    # __len__: Define el comportamiento de len() sobre el objeto, en este caso devolverá la longitud del nombre
    def __len__(self):
        return len(self._nombre)

# Ejemplo de uso de la clase Persona con los métodos dunder

p1 = Persona("Ivan", 30)  # Se llama automáticamente a __init__
p2 = Persona("Ana", 25)

# Uso de __str__ para imprimir el objeto de manera legible
print(p1)  # Salida: Nombre: Ivan, Edad: 30

# Uso de __repr__ para obtener una representación oficial del objeto
print(repr(p1))  # Salida: Persona(nombre='Ivan', edad=30)

# Uso de __eq__ para comparar dos objetos Persona
print(p1 == p2)  # Salida: False (Ivan no es igual a Ana)

# Uso de __add__ para sumar las edades de dos objetos Persona
print(p1 + p2)  # Salida: 55 (suma de las edades 30 + 25)

# Uso de __len__ para obtener la longitud del nombre
print(len(p1))  # Salida: 4 (la longitud del nombre "Ivan")

# Modificación de atributos mediante los setters
p1.nombre = "Carlos"
print(p1)  # Salida: Nombre: Carlos, Edad: 30

# Intento de asignar un valor inválido al setter de 'edad' (esto generará un ValueError)
try:
    p1.edad = -5
except ValueError as e:
    print(e)  # Salida: La edad debe ser un entero positivo
