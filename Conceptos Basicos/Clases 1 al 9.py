#CLASE 4
#Primer Print en python 
print("Hola mundo");

#CLASE 5 Variables
"""Las variables se ven como etiquetas en las que se pueden guardar valores
La estructura de las variables son <nombre> = <valor> no hace falta declarar el tipo de variable ya sea int, string etc.
Las variables deben ser nombre claros y que sigan la estructura de minusculaMayusculaPrimeraLetra, si no hay caso utilizar _ o guiones.
Se puede usar snakeCase que es titulo_curso al conformarse con dos palabras se usa el guión bajo."""

curso = 'Curso Profesional de Python';
anioCurso = 1;
print("El curso es : ",curso," cuya duracion es de ",anioCurso," año/s");


#CLASE 6 Constantes
"""Declaracion de constantes : Una constante es una variable que no puede modificar su valor, es decir toma un valor
inicial y se queda con ese valor en Python las constantes no existen, por lo que se sigue una convencion entre desarrolladores el cual es
escribir todas las letras en mayusculas por ejemplo : TITULO_CURSO = 'Curso Profesional de Python'
tener en cuenta que esto es unicamente una convencion para que se entienda que son constantes
este tipo de variables se usa unicamente para LECTURA Y NO ESCRITURA"""
TITULO_CURSO = 'Curso profesional de Python';
print(TITULO_CURSO);

#CLASE 7 Palabras reservadas en Python
"""Son aquellas palabras que no se pueden utilizar para nombrar a variables funciones o clases pues son reservadas
del lenguaje y tienen un significado o uso dentro del mismo, entre ellas estan :
False	class	is	return
None	continue	lambda	try
True	def	nonlocal	while
and	del	not	with
as	elif	or	yield
assert	else	pass	*
break	except	raise	*

Existen otras palabras reservadas en Python pero entre las mas comunes destacamos esas."""

#CLASE 8 Comentarios
"""Para dejar comentarios en Python se puede hacer con Triples comillas dobles al comienzo y al final
para poner comentarios de mas de una linea y #comentarioRealizado para comentarios de una sola linea"""
#Comentario de una Linea
"""Comentario
de 
mas de una linea"""

#CLASE 9 Tipos de Datos
"""En esta clase se va trabajar con 4 tipos de datos que son
String = Cadenas
Int = Enteros
Float = Flotantes
Bool = Booleano"""
#Strings
titulo_curso = 'Curso Profesional de Python';
print(titulo_curso);
nombreCompleto = "Ivan Sanchez";
print("El nombre completo es: ",nombreCompleto);
mensaje = '"CodigoFacilito"'; #Se puede incluir asi comillas dobles en los strings.
print(mensaje);
#Si queremos que tenga salto de lineas entonces triple comillas simples o triple comillas dobles
mensaje2 = '''Te encuentras en el curso
de Python
de Codigo Facilito'''
print(mensaje2);

#Int
numeroDePrueba = 90
print("El numero INT de prueba es : ",numeroDePrueba);
#Si queremos sacar la parte entera de una division basta con usar doble slash
numeroPrueba2 = 90//7; #en vez de estirar 12.857142857142858 estira solo 12
print(numeroPrueba2);

#Float
numero_dos = 3.14;
print("El numero con decimal es : ",numero_dos);


#Bool
#Ambos se escriben en mayusculas tanto True o False
valor = True;
print(valor);
valor = False;
print(valor);
