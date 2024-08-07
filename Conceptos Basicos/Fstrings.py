#El uso de Fstrings permite que podamos crear nuevas cadenas a partir de otras
nombre = 'Ivan Alfredo'
apellido = 'Sanchez Rojas'

nombre_completo = nombre+' '+apellido
print(nombre_completo)

nombre_completo_f = f'Mr . {nombre} {apellido}' #Es como concatenar a ese String existente otro valor String
#esto se denomina interpolacion.
print(nombre_completo_f)