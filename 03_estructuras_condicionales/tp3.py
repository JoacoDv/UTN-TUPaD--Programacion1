import random
from statistics import mode, median, mean

# Ejercicio 1:

edad = int(input("Introduzca su edad: "))

if edad >= 18:
    print("Es mayor de edad.\n")

# Ejercicio 2

nota = int(input("Introduzca su calificación: "))

if nota >= 6:
    print("Aprobado\n")
else:
    print("Desaprobado\n")

# Ejercicio 3:

n = int(input("Introduzca un numero: "))

if n % 2 == 0:
    print("Ha ingresado un numero par\n")
else:
    print("Por favor ingrese un numero par\n")

# Ejercicio 4:

edad = int(input("Introduzca su edad: "))

if edad >= 0 and edad < 12:
    print("Eres un niño\n")
elif edad >= 12 and edad < 18:
    print("Eres un adolescente\n")
elif edad >= 18 and edad < 30:
    print("Eres un adulto joven\n")
elif edad >= 30:
    print("Eres un adulto\n")
else:
    pass

# Ejercicio 5:

contraseña = input("Ingrese una contraseña entre 8 y 14 caracteres: ")
longitud_contraseña = len(contraseña)

if longitud_contraseña >= 8 and longitud_contraseña <= 14:
    print("Ha ingresado una contraseña correcta\n")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres\n")

# Ejercicio 6:

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo")
elif media == mediana and mediana == moda:
    print("No hay sesgo")

# Ejercicio 7:

frase = input("Introduzca una frase: ")
letra_final = frase[-1].lower()

if letra_final == 'a' or letra_final == 'e' or letra_final == 'i' or letra_final == 'o' or letra_final == 'u':
    print(frase + '!\n')
else:
    print(frase + '\n')

# Ejercicio 8:

nombre = input("Ingrese su nombre: ")
print("Eliga una opcion:")
print("1 para la devolucion de su nombre en Mayusculas.")
print("2 para la devolucion de su nombre en Minusculas.")
print("3 para la devolucion de su nombre con la primera letra en mayuscula y el resto en minusculas.")
opcion = int(input("Su opcion: "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("La opcion elegida fue incorrecta.")

# Ejercicio 9:

terremoto = int(input("Introduzca la medida de su terremoto: "))

if terremoto < 3:
    print('"Muy leve" (imperceptible).  ')
elif terremoto >= 3 and terremoto < 4:
    print(' "Leve" (ligeramente perceptible).')
elif terremoto >= 4 and terremoto < 5: 
    print('"Moderado" (sentido por personas, pero generalmente no causa daños).')
elif terremoto >= 5 and terremoto < 6:
    print('"Fuerte" (puede causar daños en estructuras débiles).')
elif terremoto >= 6 and terremoto < 7:
    print(' "Muy Fuerte" (puede causar daños significativos).')
elif terremoto >= 7:
    print('"Extremo" (puede causar graves daños a gran escala).')

# Ejercicio 10:

dia = int(input("introduzca el dia en numero: "))
mes = int(input("introduzca el mes en numero: "))
hemisferio = input("Introduzca su hemisferio: ")

if hemisferio.lower() == "norte":
    if mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia <= 20:
        print("Invierno")
    elif mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia <= 20:
        print("Primavera")
    elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia <= 20:
        print("Verano")
    elif mes == 9 and dia >= 21 or mes == 10 or mes == 11 or mes == 12 and dia <= 20:
        print("Otoño")

elif hemisferio.lower() == "sur"
    if mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia <= 20:
        print("Verano")
    elif mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia <= 20:
        print("Otoño")
    elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia <= 20:
        print("Invierno")
    elif mes == 9 and dia >= 21 or mes == 10 or mes == 11 or mes == 12 and dia <= 20:
        print("Primavera")