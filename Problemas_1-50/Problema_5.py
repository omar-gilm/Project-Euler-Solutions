"""
2520 es el número más pequeño que puede ser dividido por cada uno de los
números del 1 al 10 sin que tengamos ningún residuo.

¿Cuál es el número positivo más pequeño que es divisible por todos los
números del 1 al 20?
"""
# Importamos el paquete necesario para usar la función gcd()
import math

# Empezamos nuestro producto con la unidad
num = 1

# Repetimos el siguiente ciclo para los enteros del 1 al 20
for i in range(1, 21):

	""" Reasignamos num al producto de num con i y después dividimos entre
	el posible común divisor de num e i para evitar factores extra
	"""
	num = num * i // math.gcd(i, num)

# Mostramos el resultado
print(num)

# Respuesta 232792560