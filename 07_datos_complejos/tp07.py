# Estructura de datos complejas:

# 1 modificar añadiendo items a diccionario

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)

# 2 Modificar actualizando valores a diccionario

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

# 3 Convertir diccionario a lista

lista_precio_frutas = list(precios_frutas.keys())

print(lista_precio_frutas)

# 4 almacenar numeros de telefono

numeros = {}

for i in range(5):
    numeros[input("Introduce el nombre del contacto a almacenar: ")] = int(input("Introduce el numero del contacto a almacenar: "))

print(numeros)

# 5 frase a diccionario y set

frase = input("Introduzca una frase: ")

palabras = frase.split()  
palabra_unica = set(palabras)
recuento = {}

for palabra in palabra_unica:
    recuento[palabra] = palabras.count(palabra)

print(palabra_unica)
print(recuento)

# 6 promedio de tres alumnos

alumnos = {}

for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = input("Ingrese las notas del alumno separadas por espacios: ").split()
    notas = tuple(map(float, notas))  # convierte cada nota a número
    alumnos[nombre] = notas

print(alumnos)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: promedio = {promedio:.2f}")

# 7 lista de estudiantes de dos parciales:

parcial1 = {1, 2, 3, 4}
parcial2 = {3, 4, 5, 6}

ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los parciales:", solo_uno)

al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)


# 8 stock diccionario

productos = {
    "clavos": 500,
    "tornillos": 400,
    "bulones": 200
}

while True:
    print("""1 Ver stock de un producto
2 Modificar stock de producto
3 Agregar producto (con stock incluido)
4 Salir""")
    respuesta = input("Eliga una opcion: ")

    if respuesta == "1":
        producto = input("Ingrese el nombre del producto: ").lower()
        if producto in productos:
            print(f"El producto {producto} tiene {productos[producto]} unidades.")
        else:
            print(f"El producto {producto} no existe en el catalogo.")

    elif respuesta == "2":
        producto = input("Introduzaca el producto a modificar: ").lower()
        if producto in productos:
            productos[producto] = int(input("Introduzca stock del producto: "))
        else:
            print("El producto no esta en el catalogo")
    elif respuesta == "3":
        productos[input("Introduzca el nombre del nuevo producto: ").lower()] = int(input("Introduzca el stock del nuevo producto: "))
    elif respuesta == "4":
        break
    else:
        print("Opcion invalida")


# 9 agenda diccionario con claves tuplas:

agenda = {
    ("Lunes", "9:00"): "Matemática",
    ("Lunes", "11:00"): "Programación 1",
    ("Martes", "10:00"): "AYSO",
    ("Miércoles", "14:00"): "OE"
}

while True:
    print("""
1 Ver toda la agenda
2 Consultar un evento
3 Salir
""")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        print("\nAgenda completa:")
        for (dia, hora), evento in agenda.items():
            print(f"{dia} {hora} - {evento}")

    elif opcion == "2":
        dia = input("Ingrese el día: ").capitalize()
        hora = input("Ingrese la hora (ej. 9:00): ")
        clave = (dia, hora)
        if clave in agenda:
            print(f"En {dia} a las {hora} hay: {agenda[clave]}")
        else:
            print(f"No hay eventos programados para {dia} a las {hora}")

    elif opcion == "3":
        break

    else:
        print("Opción no válida. Intente nuevamente.")

# 10 invertir diccionario con paises y capitales: 

# Diccionario original
paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
}

capitales = {capital: pais for pais, capital in paises.items()}

print(capitales)