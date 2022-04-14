"""
Cada nuevo termino en la secuencia de Fibonacci es generado al sumar los
dos terminos previos. Empezando con 1 y 2, los primeros 10 términos son:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Considerando los términos de la secuencia de Fibonacci cuyo valor no
excede 4 millones, encuentra la suma de los términos pares.
"""

# No hemos considerado ningún término, así que la suma empieza en 0
sum = 0

# Definimos dos variables que corresponden a los primeros dos términos
x = 1
y = 2

# Mientras x no exceda los 4000000
while x <= 4000000:
	# Si x es par se añade a sum
	if x % 2 == 0:
		sum = sum + x
	# Redefinimos para generar los elementos de la secuencia de Fibonacci
	x, y = y, x + y

# Mostramos el resultado de la suma
print(sum)

# Resultado 4613732