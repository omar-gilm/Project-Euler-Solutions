"""
La suma de los cuadrados de los primeros 10 números naturales es 
1^2 + 2^2 + ... + 10^2 = 385

El cuadrado de la suma de los primeros diez números naturales es
(1 + 2 + ... + 10)^2 = 3025

Por lo tanto la diferencia entre la suma de los cuadrados de los primeros diez números naturales y ek cuadrado de la suma es 3025 - 385 = 2640.

Encuentra la diferencia entre la suma de los cuadrados de los primeros 100 números naturales y el cuadrado de su suma.
"""

# Definimos dos variables que empiezan con valor 0

# La suma de los cuadrados de los números naturales
sum1 = 0
# La suma de los números naturales
sum2 = 0

# Ciclo que recorre los números naturales del 1 al 100
for i in range(1,101):
	
	# Sumamos los cuadrados
    sum1 = sum1 + i**2
    
    # Sumamos los números naturales
    sum2 = sum2 + i
    
# Imprime la diferencia absoluta (abs()) de la suma de los cuadrados y el cuadrado de la suma    
print(abs((sum1)-(sum2)**2))

# Resultado 25164150