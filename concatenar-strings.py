nombre = input("Ingrese el nombre : ")
apellido = input("Ingrese el apellido : ")

#nombre_completo = 'Mr' + nombre + ' '+ apellido

nombre_completo = 'Mr. ' + nombre +' '+ apellido #Se concatena mediante el simbolo de '+'
print(nombre_completo)

#Otra forma de concatenar es mediante %s

nombre_completo2 = 'Mr. %s %s' %(nombre,apellido)
print(nombre_completo2)

#Metodo format en cadenas
#Esto se acopla al uso de placeholders o llaves para decir que en ese placeholder va a estar las variables que le
#pasaremos como parametro a format.
nombre_completo = 'Mr. {} {}'.format(nombre , apellido)
print("Nombre con placeholders es : ",nombre_completo)