#Metodo de Resolución Ordenado.
#Concepto importante dentro de las herencias multiples, para tener en cuenta usamos el siguiente ejemplo
class A:
    def hablar(self):
        print("Hola desde A")
    
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass

prueba = D()
prueba.hablar()