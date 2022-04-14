"""
Los factores primos de 13195 son 5, 7, 13 y 29.
¿Cual es el factor primo más grande del número 600851475143?
"""

# Primero definimos el número del cual buscaremos los factores.
num = 600851475143

# i tomará los valores de los factores primos. Empieza con 2.
i = 2

# Nos aseguramos que i^2 no sea mayor que n
while i * i < num:
	# Mientras n sea divisible por i.
	while num % i == 0:
		# Redefinimos num para "quitar" el factor i las veces necesarias
		num = num / i
	# Hacemos que i crezca con cada ciclo
	i = i + 1

# Mostramos el resultado cuando acaben todos los ciclos
print(num)

# Resultado 6587