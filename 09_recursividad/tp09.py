# Ejercicio 1

def factorial(n):
    # Caso base
    if n == 0 or n == 1:
        return 1
    else:
        # Llamada recursiva
        return n * factorial(n - 1)

# Pedir número al usuario
num = int(input("Ingresa un número entero positivo: "))

# Mostrar factoriales desde 1 hasta num
print(f"\nFactoriales del 1 al {num}:")
for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")


# Ejercicio 2

def fibonacci(n):
    # Caso base
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Llamada recursiva
        return fibonacci(n - 1) + fibonacci(n - 2)


# Pedir número al usuario
pos = int(input("Ingresa la posición hasta la que quieres ver la serie de Fibonacci: "))

# Mostrar la serie completa
print(f"\nSerie de Fibonacci hasta la posición {pos}:")
for i in range(pos + 1):
    print(f"F({i}) = {fibonacci(i)}")


# Ejercicio 3

def potencia(base, exponente):
    # Caso base
    if exponente == 0:
        return 1
    else:
        # Llamada recursiva
        return base * potencia(base, exponente - 1)


# Algoritmo general: pedir datos al usuario
base = float(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente (entero no negativo): "))

resultado = potencia(base, exponente)

print(f"\n{base} elevado a la {exponente} = {resultado}")

# EJercicio 4

def decimal_a_binario(n):
    # Caso base
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        # División entera por 2 (//) y concatenación del resto
        return decimal_a_binario(n // 2) + str(n % 2)


# Algoritmo general
numero = int(input("Ingresa un número entero positivo en base decimal: "))

if numero < 0:
    print("Por favor, ingresa un número positivo.")
else:
    binario = decimal_a_binario(numero)
    print(f"\nEl número {numero} en binario es: {binario}")


# Ejercicio 5

def es_palindromo(palabra):
    # Caso base: una sola letra o cadena vacía siempre es palíndromo
    if len(palabra) <= 1:
        return True
    else:
        # Comparamos primera y última letra
        if palabra[0] == palabra[-1]:
            # Llamada recursiva con la palabra "recortada"
            return es_palindromo(palabra[1:-1])
        else:
            return False


# Algoritmo general
texto = input("Ingresa una palabra (sin espacios ni tildes): ").lower()

if es_palindromo(texto):
    print(f"{texto} es un palíndromo.")
else:
    print(f"'{texto} no es un palíndromo.")


# Ejercicio 6

def suma_digitos(n):
    # Caso base: si n es un solo dígito
    if n < 10:
        return n
    else:
        # Último dígito + suma de los dígitos restantes
        return (n % 10) + suma_digitos(n // 10)


# Algoritmo general
numero = int(input("Ingresa un número entero positivo: "))

if numero < 0:
    print("Por favor ingresa un número positivo.")
else:
    resultado = suma_digitos(numero)
    print(f"\nLa suma de los dígitos de {numero} es: {resultado}")


# Ejercicio 7

def contar_bloques(n):
    # Caso base
    if n == 1:
        return 1
    else:
        # Nivel actual + bloques de los niveles superiores
        return n + contar_bloques(n - 1)


# Algoritmo general
nivel_inferior = int(input("Ingresa el número de bloques en el nivel más bajo: "))

if nivel_inferior <= 0:
    print("Por favor, ingresa un número positivo.")
else:
    total_bloques = contar_bloques(nivel_inferior)
    print(f"\nTotal de bloques necesarios: {total_bloques}")


# EJercicio 8

def contar_digito(numero, digito):
    # Caso base: si el número es 0
    if numero == 0:
        return 0
    else:
        # Comprobamos el último dígito y llamamos recursivamente con el resto
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)


# Algoritmo general
num = int(input("Ingresa un número entero positivo: "))
dig = int(input("Ingresa un dígito (0-9): "))

if num < 0 or dig < 0 or dig > 9:
    print("Por favor, ingresa un número positivo y un dígito válido (0-9).")
else:
    cantidad = contar_digito(num, dig)
    print(f"\nEl dígito {dig} aparece {cantidad} veces en el número {num}.")

