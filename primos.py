'''Oriol Jiménez Garrich
'''


# Devuelve True si su argumento es primo, y False si no lo es.
def esPrimo(numero):
	div = 2
	if numero <= 0:
		return False
	elif numero == 1:
		return True
	while numero > div:
		if (numero % div == 0):
			return False
		div += 1
	return True

print(f"El numero 9 es primo? {esPrimo(9)}")
print(f"El numero 4 es primo? {esPrimo(4)}")
print(f"El numero 13 es primo? {esPrimo(13)}")
print(f"El numero 17 es primo? {esPrimo(17)}")
print(f"El numero 31 es primo? {esPrimo(31)}")

# Devuelve una tupla con todos los números primos menores que su argumento.
def primos(numero):
	results = []
	i = 2

	while i < numero:
		if esPrimo(i):
			results.append(i)
		i += 1
	return tuple(results) 

print(f"Los numeros primos menores que 10 son: {primos(10)}")
print(f"Los numeros primos menores que 20 son: {primos(20)}")
print(f"Los numeros primos menores que 40 son: {primos(40)}")
print(f"Los numeros primos menores que 50 son: {primos(50)}")

# Devuelve una tupla con la descomposición en factores primos de su argumento.
def descompon(numero):
	results = []
	i = 0
	num_primos = primos(numero)
	if (esPrimo(numero)):
		results.append(numero)
		return tuple(results)
	while numero > 1:
		if numero % num_primos[i] == 0:
			numero //= num_primos[i]
			results.append(num_primos[i])
		else:
			i += 1
	return tuple(results)


print(f"La descomposición en numeros primeros de 10 es: {descompon(10)}")
print(f"La descomposición en numeros primeros de 1447 es: {descompon(1447)}")
print(f"La descomposición en numeros primeros de 89 es: {descompon(89)}")