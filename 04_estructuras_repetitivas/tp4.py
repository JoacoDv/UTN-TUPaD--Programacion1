import random

# Ejercicio 1:

for i in range(1,101):
    print(f"{i}\n")

# Ejercicio 2:

n = int(input("Eliga un numero: "))
count = 0

if n == 0:
    count = 1
else:
    while n != 0:
        n = n // 10
        count += 1

print(f"su numero tiene {count} digitos.\n")

# Ejercicio 3:

n1 = int(input("Eliga un numero: "))
n2 = int(input("Eliga un segundo numero: "))
suma = 0
if n1 < n2:
    for i in range(n1 + 1, n2):
        suma += i
elif n1 > n2:
    for i in range(n2 + 1, n1):
        suma += i
else:
    suma = 0

print(f"La suma de los valores entre {n1} y {n2} es igual a {suma}\n")

# Ejercicio 4:

n = 1
suma = 0

while n != 0:
    n = int(input("ingrese un numero, si quiere finalizar ingrese 0: "))
    suma += n

print(f"La suma de los numeros ingresados es igual a {suma}\n")


# Ejercicio 5:

numero_adivinar = random.randint(0,9)
guess = 10
intentos = 0

while numero_adivinar != guess:
    guess = int(input("Intente adivinar el numero: "))
    intentos += 1

print(f"Felicidades adivino el numero en {intentos} intentos\n")


# Ejercicio 6:

for i in range(100, -1, -2):
    print(f"{i}\n")

# Ejercicio 7:

num = int(input("Eliga un numero entero positivo: "))

for i in range(0, num+1):
    print(f"{i}\n")



# Ejercicio 8:

num_positivo = 0
num_negativo = 0
num_par = 0
num_impar = 0

for i in range(100):
    num = int(input("Seleccione un numero: "))
    if num < 0:
        num_negativo -= 1
    if num > 0:
        num_positivo += 1
    if num % 2 == 0:
        num_par += 1
    if num % 2 != 0:
        num_impar += 1
 
print(f"""El conteo de sus 100 numeros es de:
{num_negativo} numeros negativos
{num_positivo} numeros positivos
{num_impar} numeros impares
{num_par} numeros pares
""")


# Ejercicio 9:

media = 0

for i in range(100):
    num = int(input("Ingrese un numero: "))
    media += num

media = media / 100

print(f"la media de sus numeros elegidos es de {media}\n")


# Ejercicio 10:

numero = int(input("Ingrese un numero: "))
numero_invertido = 0

while numero != 0:
    resto = numero % 10
    numero = numero // 10
    numero_invertido = numero_invertido * 10 + resto
print(f"su numero invertido es igual a {numero_invertido}")