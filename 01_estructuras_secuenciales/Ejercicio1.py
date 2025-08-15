import math

# Programa 1:
print("Hola Mundo!\n")

# Programa 2:
nombre = input("Nombre: ")
print(f'Hola {nombre}!\n')

# Programa 3:
nombre = input('Nombre: ')
apellido = input('Apellido: ')
edad = input('Edad: ')
residencia = input('Lugar de residencia: ')

print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}\n')

# Programa 4:
radio = float(input('Radio: '))
area = math.pi * radio**2
perimetro = 2 * math.pi * radio
print(f'Área: {area:.2f}\nPerímetro: {perimetro:.2f}\n')

# Programa 5:
segundos = float(input("Segundos: "))
horas = segundos / (60 * 60)
print(f'{segundos} segundos equivalen a {horas:.2f} horas.\n')

# Programa 6:
n = int(input('Número: '))
for i in range(11):
    print(f'{n} x {i} = {n * i}\n')

# Programa 7:
print("Ingrese dos números distintos de cero.\n")
n1 = 0
n2 = 0
while n1 == 0 or n2 == 0:
    n1 = int(input('Número 1: '))
    n2 = int(input('Número 2: '))

print(f'{n1} + {n2} = {n1 + n2}\n')
print(f'{n1} * {n2} = {n1 * n2}\n')
print(f'{n1} - {n2} = {n1 - n2}\n')
print(f'{n1} / {n2} = {n1 / n2:.2f}\n')

# Programa 8:
peso = int(input('Ingrese su peso (kg): '))
altura = float(input('Ingrese su altura (m): '))
IMC = peso / (altura ** 2)
print(f'Su índice corporal es de {IMC:.2f}\n')

# Programa 9:
temperatura = float(input('Ingrese su temperatura actual en Celsius: '))
f = 9/5 * temperatura + 32
print(f'Su temperatura en grados fahrenheit es de {f:.2f}')

# Programa 10:
print('Ingrese tres numeros.\n')
n1 = float(input('Numero 1: '))
n2 = float(input('Numero 2: '))
n3 = float(input('Numero 3: '))
average = (n1 + n2 + n3) / 3
print(f'Su promedio es de {average:.3f}\n')