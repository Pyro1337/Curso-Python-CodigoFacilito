# Creacion de la clase Celular.
class Celular: 
    def __init__(self, marca, modelo, camara): # Creacion de constructores
        # Definimos los atributos, utilizamos self para referirnos al this.atributo = atributo que se usa en Java.
        self.marca = marca
        self.modelo = modelo
        self.camara = camara


#Definicion de funciones de este objeto.
    def llamar(self, numero):  # Añadir self
        print("Se esta llamando al numero " + numero)

    def cortar(self, numero):  # Añadir self
        print("Colgaste la llamada con " + numero)

    def fotografiar(self, cantidad):  # Añadir self
        print("Se capturaron correctamente las " + str(cantidad) + " fotos")

celu1 = Celular("Samsung", "j7", "32Mpx") # Instanciamos
print("Marca: " + celu1.marca + "\nModelo: " + celu1.modelo + "\nCamara: " + celu1.camara) # Imprimimos los elementos de ese objeto.
celu1.llamar("0984650492")
celu1.cortar("0984650492")
celu1.fotografiar(5) 

