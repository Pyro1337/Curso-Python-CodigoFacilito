#Para obtener valores por teclado usaremos la funcion input("Mensaje de contexto de ingreso: ");
#input("Ingresa tu nombre completo: ");
#para almacenarlo en una variable basta con variable = input ("Mensaje de contexto de ingreso ");
nombreCompleto = input("Ingrese el nombre completo: ")
print("El nombre completo es : ",nombreCompleto)
#Tener en cuenta que input siempre retorna un tipo de dato STR esto se confirma si se hace lo siguiente : 
print(type(nombreCompleto))

#convertir tipos de datos
#Como se estuvo explicando, las variables al ser ingresada mediante inputs por teclado se guardan como Str, lo cual no es correcto
#por ende hay que convertir al tipo de dato correspondiente por ejemplo de la siguiente forma.
edad = input("Ingrese la edad : ")
edad = int(edad)
print("La edad es : ",edad)
print(type(edad)) #aqui si ya muestra que es int

altura = input("Ingrese la altura : ")
altura = float(altura)
print("La altura es : ",altura)
print(type(altura))

autorizacion = input("¿Autorizas el programa? (si/no): ")
autorizacion = autorizacion == 'si' #esto indica que el true va ser al colocar si.
autorizacion = bool(autorizacion)
print("El resultado de la autorizacion es : ",autorizacion)
print(type(autorizacion))
