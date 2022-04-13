# Problema 1

"""
Si enlistamos todos los números naturales menores a 10 que son multiplos de 3
o 5, obtenemos 3, 5, 6 y 9. La suma de estos multiplos es 23.

Encuentra la suma de todos los multiplos de 3 o 5 que sean menores de 1000.
"""

# Definimos la variable que almacenará la suma que nos interesa
sum = 0 

# Ciclo que itera sobre cada entero entre 0 y 1000
for num in range(1000): 

	# Si num es multiplo de 3 o 5, lo sumamos a sum
	if num % 3 == 0 or num % 5 == 0:
		
		# sum sigue creciendo
		sum = sum + num 

# Imprime el resultado
print(sum)

# Resultado 233168 