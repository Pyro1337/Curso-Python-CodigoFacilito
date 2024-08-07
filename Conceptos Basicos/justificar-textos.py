mensaje = 'Hola Mundo!'

#ljust -> Justifica a la izquierda
#rjust -> Justifica a la derecha
#center -> Centra
#Atencion que estos metodos no reemplazan sino que crean uno nuevo, pues los strings son inmutables.
#Reciben como argumento la cantidad de espacios.
mensaje = mensaje.ljust(20)
print(mensaje)
mensaje = mensaje.rjust(20)
print(mensaje)
mensaje = mensaje.center(20)
print(mensaje)
