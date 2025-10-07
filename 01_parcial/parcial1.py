# Programa para contabilizar los lirbos en una biblioteca

titulos = []
ejemplares = []

print("Bienvenido al gestor de libros")
print("Esata son sus opciones disponibles")

while True:

    print("""1 Ingresar titulos
2 Ingresar ejemplares
3 Mostrar catalogo
4 Consultar disponibilidad
5 Listar agotados
6 Agregar titulo
7 Actualizar ejemplares
8 Salir
""")

    eleccion = input("Decida que desea hacer y ingrese el numero de su opcion: ")
    print("-------------------------------------------------------\n\n")

    if eleccion == '1':
        titulo_nuevo = input("Ingrese el titulo que desea añadir: ")
        for titulo in titulos:
            if titulo == titulo_nuevo.lower():
                print("Ese titulo ya esta registrado\n")
                break
            else:
                continue
        titulos.append(titulo_nuevo.lower())
        ejemplares.append(0)
        print(f"Titulo: {titulo_nuevo.lower()} añadido con exito.\n\n")

    elif eleccion == '2':
        if not titulos:
            print("No hay titulos disponibles.\n\n")
            continue
        while True:
            print("Elija el título del cual quiere ingresar ejemplares.")
            titulo_elegido = input("Ingrese el título: ").lower()

            if titulo_elegido not in titulos:
                print("El título elegido no se encuentra registrado.\n")
                continue

            ejemplares_elegidos = input("Ingrese la cantidad de ejemplares: ")

            if not ejemplares_elegidos.isdigit():
                print("La cantidad de ejemplares ingresada no es un número.\n")
                continue

            ejemplares_elegidos = int(ejemplares_elegidos)

            if ejemplares_elegidos < 0:
                print("La cantidad de ejemplares no puede ser negativa.\n")
                continue

            indice = titulos.index(titulo_elegido)
            ejemplares[indice] = ejemplares_elegidos
            print(f"Ejemplares de {titulo_elegido} actualizados a {ejemplares_elegidos}.\n\n")
            break

    elif eleccion == '3':
        if not titulos:
            print("No hay titulos disponibles.\n")
            continue
        for titulo in titulos:
            indice = titulos.index(titulo)
            print(f"{indice + 1} {titulo}, {ejemplares[indice]} ejemplares")
        print("\n\n")            

    elif eleccion == '4':
        if not titulos:
            print("No hay titulos disponibles.\n")
            continue
        titulo_busqueda = input("Ingrese el titulo del cual quiere saber disponibilidad: ").lower()
        if titulo_busqueda not in titulos:
            print(f"{titulo_busqueda.lower()} no se encuentra en la seleccion de titulos.\n\n")
            continue
        for titulo in titulos:
            if titulo == titulo_busqueda.lower():
                print(f"El titulo {titulo} tiene {ejemplares[titulos.index(titulo)]} disponibles\n\n")

    elif eleccion == '5':
        if not titulos:
            print("No hay titulos disponibles.\n")
            continue
        titulos_agotados = False
        for titulo in titulos:
            if ejemplares[titulos.index(titulo)] == 0:
                titulos_agotados = True
                break
        
        if not titulos_agotados:
            print("No hay titulos agotados \n\n")
            continue
        else:
            for titulo in titulos:
                if ejemplares[titulos.index(titulo)] == 0:
                    print(f"{titulo} agotado")
        print("\n\n")

    elif eleccion == '6':
        titulo_nuevo = input("Escriba el titulo a añadir: ").lower()
        if titulo_nuevo in titulos:
            print("Disculpe el titulo ya esta en la seleccion de titulos. \n\n")
            continue
        ejemplares_nuevo = 0
        while True:
            ejemplares_nuevo = input("Escriba la cantidad de ejemplares del titulo: ")
            if not ejemplares_nuevo.isdigit():
                print("Lo siento eliga un numero.")
                continue
            elif int(ejemplares_nuevo) < 0:
                print("Lo siento ingrese un numero a partir de 0")
                continue
            break
        titulos.append(titulo_nuevo)
        ejemplares.append(ejemplares_nuevo)
        print(f"El titulo {titulo_nuevo} con {ejemplares_nuevo} fue añadido a la coleccion \n\n")

    elif eleccion == '7':
        if not titulos:
            print("No hay titulos disponibles.\n")
            continue
        print("Ingrese el titulo del cual quiere hacer un prestamo/devolucion")

        titulo_seleccionado = input("Escriba el titulo: ").lower()

        if titulo_seleccionado not in titulos:
            print("Disculpe el titulo seleccionado no esta en la coleccion.\n\n")
            continue

        print("""1 para hacer un prestamo
2 para realizar una devolucion""")

        while True:
            respuesta = input("Eliga la opcion deseada: ")
            indice = titulos.index(titulo_seleccionado)

            if respuesta == '1':
                if ejemplares[indice] > 0:
                    ejemplares[indice] -= 1
                    print(f"El titulo {titulo_seleccionado} ahora cuenta con {ejemplares[indice]} ejemplares\n\n")
                    break
                else:
                    print("Lo siento yano quedan ejemplares disponibles para realizar el prestamo.\n\n")
                    break
            elif respuesta == '2':
                ejemplares[indice] += 1
                print(f"El titulo {titulo_seleccionado} ahora cuenta con {ejemplares[indice]} ejemplares\n\n")
                break

    elif eleccion == '8':
        print("Gracias por utilizar el programa. Hasta luego!\n\n")
        break