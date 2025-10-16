# 1 Creamos archivo inicial con tres productos si es que no existe

# importamos la biblioteca os
import os

# asignamos el nombre del archivo
nombre_archivo = "productos.txt"

# Verificamos si el archivo existe
if not os.path.exists(nombre_archivo):
    # Si no existe, lo creamos
    with open(nombre_archivo, "w") as archivo:
        archivo.write("supra mk4,32.000,2\nimpreza,26.000,3\nskyline,40.000,1\n")
    print("Archivo creado:", nombre_archivo)


# 2 Leemos y mostramos los productos

# Abrimos para leer el archivo
with open(nombre_archivo, "r") as archivo:
    # Leemos todas las lineas
    lineas = archivo.readlines()
    # Iteramos la lista de lineas
    for linea in lineas:
        # Extraemos los datos
        datos = linea.strip().split(",")
        # asignamos los datos en variables mas claras
        nombre, precio, cantidad = datos
        # Imprimimos la linea apuntando cada dato como corresponde
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")


# 3 Agregar un producto

# Pedimos los datos necesarios al usuario
print("Agregaremos un producto nuevo al listado.")
nombre = input("Ingrese el nombre del producto: ")
precio = input("Ingrese el precio del producto separando las milesimas, millones y billones con punto: ")
cantidad = input("Ingrese la cantidad del producto: ")

# Abrimos el archivo para modificarlo (especificamos el encoding por los acentos y la ñ)
with open(nombre_archivo, "a", encoding="utf-8") as archivo:
    # Escribimos la linea como corresponde
    archivo.write(f"{nombre.lower()},{precio},{cantidad}\n")


# 4 Leer archivo y crea lista de diccionarios

# Creamos la lista vacia
productos = []

# Abrimos para leer el archivo
with open(nombre_archivo, "r") as archivo:
    # Leemos todas las lineas
    lineas = archivo.readlines()
    # Iteramos la lista de lineas
    for linea in lineas:
        # Extraemos los datos
        datos = linea.strip().split(",")
        # asignamos los datos en variables mas claras
        nombre, precio, cantidad = datos
        # Añadimos el diccionario a la lista
        productos.append({"nombre": nombre.lower(), "precio": precio, "cantidad": cantidad})

# 5 Buscar por nombre de producto

# Pedimos el producto a encontrar
producto = input("Ingrese el nombre del producto que desea buscar: ")

# Buscamos el producto
producto_filtrado = next((p for p in productos if p["nombre"].lower() == producto.lower()), None)

# Usamos una estructura condicional para indicar un error en caso de no encontrarlo 
if producto_filtrado:
    print(f"Producto: {producto_filtrado['nombre']} | Precio: ${producto_filtrado['precio']} | Cantidad: {producto_filtrado['cantidad']}")
else: 
    print("El producto no ha sido encontrado.") 

# Este sistema se podria optimizar para devolver un array similar por ejemplo si el usuario quiere buscar "honda" devolvemos un array con todos los vehiculos que incluyan "honda" en su nombre

# 6 Reescribir el archivo (no esta especificado pero damos por sentado que se utilizara la lista de diccionarios para hacerlo)

# Abirmos el archivo en modo "w"
with open(nombre_archivo, "w") as archivo:
    # Y dentro iteramos la lista de productos
    for producto in productos:
        # Escribimos la linea en el mismo orden que las guardamos
        archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")