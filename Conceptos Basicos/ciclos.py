#Ciclo While
#Creemos un programa que imprima todos los valores del 1 al 10 mediante el while
c = 1
while (c <=10) :
    print(c)
    c+= 1 #o se puede usar en su lugar c + = 1

#Ciclo For
#Creamos la lista con estos elementos
usuarios = ['Usuario1', 'Usuario2', 'Usuario3', 'Usuario4'] #Cargamos la lista de Strings
for usuario in usuarios: #Realizamos el for singular in pluralesLista e imprimimos.
    print(usuario)

#Uso de break
titulo_curso = 'Curso profesional de Python'
for caracter in titulo_curso:
    if caracter == 'P': #Si encuentra una P dentro de la cadena de caracteres entonces va cortar el ciclo for
        print("Se encuentra P dentro de la cadena, se corta el ciclo for")
        break
    print(caracter) #Esto imprimira uno por uno los caracteres incluyendo los 
    
#Uso del continue
print("Uso del continue ignorando los espacios en blanco")
for caracter in titulo_curso:
    if caracter ==" ":
        continue
    print(caracter)