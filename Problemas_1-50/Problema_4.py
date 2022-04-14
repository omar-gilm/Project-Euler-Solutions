"""
Un número palindromo se lee de la misma manera en ambos sentidos. El palindromo más grande hecho a partir del producto de dos números de 2 dígitos es 9009 = 91 x 99.

Encuentra el palindromo más grande hecho a partir del producto de dos números de 3 dígitos.
"""

# Esta función regresa true si num es un palindromo
def is_pal(num):
	return str(num) == str(num)[::-1]

# Variable que almacenará el palindromo más grande
lar = 1

# Primer factor del producto, tomará valores del 1 al 999
for num1 in range(1,1000):

	# Segundo factor del producto
	for num2 in range(1,1000):

		# num es igual al producto de los dos factores
		num = num1 * num2

		# Revisamos si num es palindromo y más grande que lar
		if is_pal(num) and num > lar:
			lar = num

""" 
Mostramos el palindromo más grande una vez hemos considerado todos los factores de tres dígitos posibles.
"""
print(lar)

# Resultado 906609