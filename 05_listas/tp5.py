import random

# Ejercicio 1:

notas = [10,5,6,2,8,9,7,7,4,10]
menor = 10
mayor = 0

for nota in notas:
    if nota < menor:
        menor = nota
    if nota > mayor:
        mayor = nota
    print(nota, end=' ')
print("")
promedio = sum(notas) / len(notas)
print(f"El promedio de las notas es {promedio}")
print(f"La mayor nota es {mayor} y la menor {menor}")


# Ejercicio 2:

productos = []

for i in range(5):
    productos.append(input("Ingrese un producto: ").title())

productos_ordenados = sorted(productos)

for producto in productos_ordenados:
    print(producto, end = ' ')
print("")

productos_ordenados.remove(input("Introduzca un producto para eliminarlo: ").title())
for producto in productos_ordenados:
    print(producto, end = ' ')
print("")


# Ejercicio 3:

numeros_aleatorios = []
pares = []
impares = []

for i in range(15):
    numeros_aleatorios.append(random.randint(1, 100))

for numero in numeros_aleatorios:
    if numero % 2 == 0:
        pares.append(numero)
    elif numero % 2 == 1:
        impares.append(numero)

print(f"Los pares en la listas son {pares} y los impares {impares}")



# Ejercicio 4: 

lista_duplicada = [1,3,5,3,7,1,9,5,3]

lista_limpia = list(set(lista_duplicada))

for numero in lista_limpia:
    print(numero, end = ' ')
print("")

# Ejercicio 5:

estudiantes = ["pedro", "abril", "ignacio", "laura", "roberto", "juan", "maria", "violeta"]

respuesta = input("""1 Para eliminar un estudiante
2 Para añadir un estudiante
3 Para no hacer ninguna
"""
)

if respuesta == 1:
    estudiantes.remove(input("Ingrese el nombre: ").lower())
elif respuesta == 2:
    estudiantes.append(input("Ingrese el nombre: ").lower())
elif respuesta == 3:
    pass
else: 
    print("La opcion seleccionada es incorrecta")

for estudiante in estudiantes:
    print(estudiante, end = ' ')
print("")


# Ejercicio 6:

lista = [12, 22, 2, 43, 5, 54, 9]

for i in range(1, (len(lista) + 1 )// 2):
    recipiente = lista[len(lista) - i]
    lista[len(lista) - i] = lista[i - 1]
    lista[i - 1] = recipiente

for numero in lista:
    print(numero, end = ' ')
print(" ")


# Ejercicio 7:

temperaturas = [[-3, 20], [-1, 18], [0, 19], [-2, 16], [0, 17], [2, 20], [1, 19]]

promedio_minimas = 0
promedio_maximas = 0
dia_mayor_amplitud = 0
mayor_amplitud = 0
i = 1

for dia in temperaturas:
    promedio_minimas += dia[0]
    promedio_maximas += dia[1]
    if dia[1] - dia[0] > mayor_amplitud:
        mayor_amplitud = dia[1] - dia[0]
        dia_mayor_amplitud = i
    i += 1

print(f"""El dia de mayor amplitud es el dia {dia_mayor_amplitud}
promedio de maximas = {promedio_maximas}
promedio de minimas = {promedio_minimas}
""")


# Ejercicio 8:

notas = [[2,8,10], [7,6,9], [10,8,6], [4,6,9], [8,3,8]]

materia1 = 0
materia2 = 0
materia3 = 0

for estudiante in notas:
    print(f"Promedio estudiante: {(estudiante[0] + estudiante[1] + estudiante[2]) / 3}")
    materia1 += estudiante[0]
    materia2 += estudiante[1]
    materia3 += estudiante[2]

print(f"""Promedio de materias: 
materia 1: {materia1}
materia 2: {materia2}
materia 3: {materia3}
""")

# Ejercicio 9:

tablero = [['-', '-', '-'],
           ['-', '-', '-'],
           ['-', '-', '-']]

def mostrar_tablero():
    for fila in tablero:
        print(" ".join(fila))
    print()

def hay_ganador(tablero, jugador):
    for fila in tablero:
        if all(celda == jugador for celda in fila):
            return True

    for col in range(3):
        if all(tablero[fila][col] == jugador for fila in range(3)):
            return True

    if all(tablero[i][i] == jugador for i in range(3)):
        return True
    if all(tablero[i][2 - i] == jugador for i in range(3)):
        return True

    return False

jugador = 'x'

while True:
    mostrar_tablero()
    print(f"Turno de {jugador}")
    fila = int(input("Elige fila (0-2): "))
    col = int(input("Elige columna (0-2): "))

    if tablero[fila][col] != '-':
        print("Esa casilla ya está ocupada, intenta otra.")
        continue

    tablero[fila][col] = jugador

    if hay_ganador(tablero, jugador):
        mostrar_tablero()
        print(f"¡Ganó {jugador}!")
        break

    if all(celda != '-' for fila in tablero for celda in fila):
        mostrar_tablero()
        print("¡Empate!")
        break

    jugador = 'o' if jugador == 'x' else 'x'


# Ejercicio 10:

ventas = [[2, 3, 1 , 4 , 5, 2 , 1], [6, 1, 0, 9, 4 , 2 , 1], [14, 2, 1, 2, 3, 4, 5], [1, 2, 65, 32, 1, 2, 23]]

productos_total = []

total = 0

dia_mas_ventas = 0

mayor = 0
mayor_indice = 0
i = 0


for producto in ventas:
    for dia in producto: 
        total += dia
    productos_total.append(total)
    total = 0

for i in range(7):
    if (ventas[0][i] + ventas[1][i] + ventas[2][i] + ventas[3][i]) > dia_mas_ventas:
        dia_mas_ventas = i + 1

print(f"El dia con mas ventas fue el dia {dia_mas_ventas}")

for producto in productos_total:
    if producto > mayor:
        mayor = producto
        mayor_indice = i
    i += 1
    print(f"Producto {i} vendio {producto} unidades")

print(f"El producto mas vendido fue el {mayor_indice} con {mayor} ventas")



        