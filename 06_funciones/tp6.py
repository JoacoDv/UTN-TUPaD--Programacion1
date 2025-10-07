# importamos la libreria math para usar en la consigna 4

import math

# 1 hola mundo

def imprimir_hola_mundo():
    #Imprimimos en pantalla hola mundo con la funcion pre-built de python print()
    print("Hola Mundo!")

# 2 Saludar al usuario

# Recibimos el nombre como parametro
def saludar_usuario(nombre):
    # Imprimimos el saludo con print y f string para concatenar la variable con el saludo
    print(f"Hola {nombre}!")

# 3 Informacion personal

def informacion_personal(nombre, apellido, edad, residencia):
    # Imprimimos un resumen de la informacion personal del usuario con los parametro ya previamentes pedidos concatenando con f string
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4 radio y perimetro del circulo

def calcular_area_circulo(radio):
    # calculamos el area como corresponde usando pi de la libreria math
    area = math.pi * (radio ** 2)
    # Luego imprimimos el resultado por pantalla y por ultimo lo retornamos, en caso de no querer retornarlo o imprimirlo se puede comentar la linea correspondiente
    print(f"El area del circulo es de {area}")

    # Repetimos el procedimiento de la funcion previa pero ajustamos los calculos a los correspondientes
def  calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    print(f"El perimetro del circulo es de {perimetro}")

# 5 segundos a horas

def segundos_a_horas(segundos):
    # validamos que no sea un numero negativo
    if segundos < 0:
        print("Lo siento no es posible convertir numeros negativos")
        return
    # convertimos los segundos a horas dividiendolo por 3600 que son los segundos que hay en una hora
    horas = segundos / 3600
    # imprimimos y retornamos el valor, aqui tambien se puede comentar la linea no deseada
    print(f"{segundos} segundos equivales a {horas} horas")
    return horas

# 6 tabla de multiplicar

def tabla_multiplicar(numero):
    # para hacer la tabla hacemos un rango de 1 hasta 10 y mostramos los resultados de la multiplicacion en pantalla
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7 tupla de operaciones basicas

def operaciones_basicas(a, b):
    # primero realizamos todas las operaciones basicas luego las imprimimos y por ultimo hacemos y devolvemos la tupla
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a // b
    print(f"""Los resultados de las operaciones basicas con {a} y {b} son:
suma = {suma}
resta = {resta}
multiplicación = {multiplicacion}
división = {division}
""")
    tupla_final = (suma, resta, multiplicacion, division)
    return tupla_final

# 8 indice de masa corporal

def calcular_imc(peso, altura):
    # calculamos peso dividido el cuadrado de la altura
    imc = peso / (altura * altura)
    print(f"Tu indice de masa corporal es de {imc}")
    return imc

# 9 convertir temperatura

def celsius_a_fahrenheit(celsius):
    # calculamos la conversion con la formula correspondiente
    farenheit = celsius * (9 / 5) + 32
    print(f"{celsius} grados celsius equivalen a {farenheit} grados farenheit")
    return farenheit

# 10 calcular promedio

def calcular_promedio(a, b ,c):
    promedio = (a + b + c) / 3
    print(f"El promedio es de {promedio}")
    return promedio

def main():
    # funcion 1
    imprimir_hola_mundo()
    #funcion 2
    saludar_usuario(input("Ingrese su nombre: "))
    #funcion 3
    # pedimos los datos del usuario dentro del scope de main evitando hacerlo dentro del llamado de la funcion para mayor legibilidad
    nombre = input("Ingrese su nombre o apodo: ")
    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))
    residencia = input("Ingrese el lugar actual donde reside: ")
    informacion_personal(nombre, apellido, edad, residencia)
    # funciones 4
    # primero pedimos el radio al usuario y luego llamamos a ambas funciones
    radio = float(input("Ingrese el radio del circulo: "))
    calcular_area_circulo(radio)
    calcular_perimetro_circulo(radio)
    # funcion 5
    segundos = int(input("Ingrese la cantidad de segundos que desea convertir: "))
    segundos_a_horas(segundos)
    # funcion 6
    numero = int(input("Ingrese un numero entero: "))
    tabla_multiplicar(numero)
    # funcion 7
    num1 = int(input("Ingrese un numero entero para operar con el: "))
    num2 = int(input("Ingrese un segundo numero entero para operar al numero anterior: "))
    operaciones_basicas(num1, num2)
    # funcion 8
    peso = float(input("Ingresa tu peso en kilogramos: "))
    altura = float(input("Ingresa tu altura en metros: "))
    calcular_imc(peso, altura)
    #funcion 9
    celsius = int(input("Ingrese su temperatura actual en grados celsius: "))
    celsius_a_fahrenheit(celsius)
    # funcion 10
    a = int(input("ingrese un numero entero: "))
    b = int(input("Ingrese un segundo numero entero: "))
    c = int(input("Ingrese un tercer numero entero: "))
    calcular_promedio(a, b, c)


main()