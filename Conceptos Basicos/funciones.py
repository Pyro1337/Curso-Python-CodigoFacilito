#Para definir funciones que retornan un valor
def suma (x,y): #Funcion declarada con parametros x e y
    return x+y


#Metodos es decir funciones que no retornan nada
def multiplicar(x,y):
    print("El resultado de multiplicarlos es :  ", x*y)


valorA = input("Ingrese el primer valor : ")
valorA = int(valorA) #convertimos a int
valorB = input("Ingrese el segundo valor : ")
valorB = int(valorB) #convertimos a int
multiplicar(valorA,valorB) #llamamos a la funcion y le pasamos los argumentos
resultado_suma = suma(valorA,valorB) #Llamamos a la funcion y le pasamos los argumentos
print("El resultado retornado de la suma es :",resultado_suma)


