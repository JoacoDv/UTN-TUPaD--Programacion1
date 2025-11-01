import csv
import os

# ---------- FUNCIONES AUXILIARES ----------

def normalizar_titulo(titulo):
    # Elimina espacios redundantes y normaliza a minúsculas.
    return " ".join(titulo.strip().lower().split())

def cargar_catalogo(nombre_archivo):
    # Carga el catálogo desde un CSV.
    # Si el archivo no existe, lo crea con encabezado y devuelve [].
    
    catalogo = []

    # Si no existe, crear archivo con encabezado y devolver catálogo vacío
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
            archivo.write("TITULO,CANTIDAD\n")
        return catalogo

    # Si existe, leerlo validando cada fila
    with open(nombre_archivo, newline="", encoding="utf-8") as archivo:
        # Hacemos uso de DictReader para leer el archivo como diccionario con el encabezado como keys
        lector = csv.DictReader(archivo)
        for fila in lector:
            titulo = fila.get("TITULO", "").strip()
            cantidad_cadena = fila.get("CANTIDAD", "").strip()

            # Validaciones: título no vacío, cantidad debe ser dígitos (entero no negativo)
            if titulo == "":
                # fila inválida: título vacío -> la ignoramos
                continue
            if not cantidad_cadena.isdigit():
                # fila inválida: cantidad no es entero no negativo -> la ignoramos
                continue

            cantidad = int(cantidad_cadena)
            if cantidad < 0:
                # no debería ocurrir porque isdigit() excluye el signo '-', pero lo chequeamos por seguridad
                continue

            catalogo.append({"TITULO": titulo, "CANTIDAD": cantidad})

    return catalogo


def guardar_catalogo(nombre_archivo, catalogo):
    # Guarda el catálogo actual en el archivo CSV.
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
        campos = ["TITULO", "CANTIDAD"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(catalogo)

def buscar_libro(catalogo, titulo):
    # Devuelve el índice del libro si existe, o -1 si no está.
    titulo_normalizado = normalizar_titulo(titulo)
    for i, libro in enumerate(catalogo):
        if normalizar_titulo(libro["TITULO"]) == titulo_normalizado:
            return i
    return -1

def solicitar_entero(mensaje):
    # Pide un número entero no negativo y lo valida.
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit():
            return int(valor)
        print("Error: Debe ingresar un número entero no negativo.")

# ---------- FUNCIONALIDADES PRINCIPALES ----------

def ingresar_titulos(catalogo):
    cantidad = solicitar_entero("¿Cuántos libros desea cargar? ")
    for _ in range(cantidad):
        while True:
            titulo = input("Ingrese el título del libro: ").strip()
            if titulo == "":
                print("El título no puede estar vacío.")
                continue
            if buscar_libro(catalogo, titulo) != -1:
                print("Ese título ya existe en el catálogo.")
                continue
            stock = solicitar_entero("Ingrese la cantidad de ejemplares disponibles: ")
            catalogo.append({"TITULO": titulo, "CANTIDAD": stock})
            print(f"Libro {titulo} agregado con {stock} ejemplares.")
            break
    return catalogo

def ingresar_ejemplares(catalogo):
    titulo = input("Ingrese el título del libro a actualizar: ")
    indice = buscar_libro(catalogo, titulo)
    if indice == -1:
        print("Libro no encontrado.")
        return catalogo
    cantidad = solicitar_entero("¿Cuántos ejemplares desea agregar? ")
    catalogo[indice]["CANTIDAD"] += cantidad
    print(f"Se agregaron {cantidad} ejemplares al libro {catalogo[indice]['TITULO']}.")
    return catalogo

def mostrar_catalogo(catalogo):
    if not catalogo:
        print("El catálogo está vacío.")
    else:
        print("\n--- CATÁLOGO COMPLETO ---")
        for libro in catalogo:
            print(f"{libro['TITULO'].title()} - {libro['CANTIDAD']} ejemplares")
    print()

def consultar_disponibilidad(catalogo):
    titulo = input("Ingrese el título a consultar: ")
    indice = buscar_libro(catalogo, titulo)
    if indice == -1:
        print("Título no encontrado.")
    else:
        cantidad = catalogo[indice]["CANTIDAD"]
        print(f"{catalogo[indice]['TITULO'].title()} tiene {cantidad} ejemplares disponibles.")

def listar_agotados(catalogo):
    agotados = [libro for libro in catalogo if libro["CANTIDAD"] == 0]
    if not agotados:
        print("No hay libros agotados.")
    else:
        print("\n--- LIBROS AGOTADOS ---")
        for libro in agotados:
            print(f"{libro['TITULO'].title()}")
    print()

def agregar_titulo(catalogo):
    titulo = input("Ingrese el nuevo título: ").strip()
    if titulo == "":
        print("El título no puede estar vacío.")
        return catalogo
    if buscar_libro(catalogo, titulo) != -1:
        print("El título ya existe.")
        return catalogo
    cantidad = solicitar_entero("Ingrese la cantidad inicial de ejemplares: ")
    catalogo.append({"TITULO": titulo, "CANTIDAD": cantidad})
    print(f"Libro {titulo} agregado correctamente.")
    return catalogo

def actualizar_ejemplares(catalogo):
    titulo = input("Ingrese el título a actualizar (préstamo/devolución): ")
    indice = buscar_libro(catalogo, titulo)
    if indice == -1:
        print("Libro no encontrado.")
        return catalogo

    print("1. Préstamo\n2. Devolución")
    opcion = input("Elija una opción: ")
    match opcion:
        case "1":
            if catalogo[indice]["CANTIDAD"] > 0:
                catalogo[indice]["CANTIDAD"] -= 1
                print(f"Préstamo realizado. Quedan {catalogo[indice]['CANTIDAD']} ejemplares.")
            else:
                print("No hay ejemplares disponibles para préstamo.")
        case "2":
            catalogo[indice]["CANTIDAD"] += 1
            print(f"Devolución registrada. Total: {catalogo[indice]['CANTIDAD']} ejemplares.")
        case _:
            print("Opción inválida.")
    return catalogo

# ---------- MENÚ PRINCIPAL ----------

def menu():
    # Al inicializar el nombre del archivo contamos con la opcion de tomarlo de un input del usuario de manera que sea mas interactivo
    nombre_archivo = "catalogo.csv"
    catalogo = cargar_catalogo(nombre_archivo)
    while True:
        print("""
======= MENÚ PRINCIPAL =======
1. Ingresar títulos (múltiples)
2. Ingresar ejemplares
3. Mostrar catálogo
4. Consultar disponibilidad
5. Listar agotados
6. Agregar título
7. Actualizar ejemplares (préstamo/devolución)
8. Salir
""")
        opcion = input("Seleccione una opción: ").strip()
        match opcion:
            case "1":
                catalogo = ingresar_titulos(catalogo)
            case "2":
                catalogo = ingresar_ejemplares(catalogo)
            case "3":
                mostrar_catalogo(catalogo)
            case "4":
                consultar_disponibilidad(catalogo)
            case "5":
                listar_agotados(catalogo)
            case "6":
                catalogo = agregar_titulo(catalogo)
            case "7":
                catalogo = actualizar_ejemplares(catalogo)
            case "8":
                print("Saliendo del sistema.")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")

        # Guardamos después de cualquier posible cambio
        guardar_catalogo(nombre_archivo, catalogo)

# ---------- EJECUCIÓN ----------
if __name__ == "__main__":
    menu()
