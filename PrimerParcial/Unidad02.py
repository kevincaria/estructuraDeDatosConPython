'''
Ejercicio 1
Escribir un procedimiento que muestre por pantalla la cadena “Hola mundo!!!” 
cada vez que se la invoque
'''
def holaMundo():
    return print('Hola mundo')

holaMundo()
'''
Ejercicio 2
Escribir un procedimiento que se le pase por parámetros una cadena 'nombre' y 
muestre por pantalla: “Hola 'nombre'!!!”
'''
def mostrarPorPantalla(nombre):
    return print(f'Hola {nombre} !!')

mostrarPorPantalla('Kevin')
'''
Ejercicio 3
Escribir   una   función   que   calcule   y   retorne   el   factorial   de   un   numero   natural.
'''

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

print(factorial(3))

'''
Ejercicio 4
Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función
debe recibir el importe sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la
factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un
21%.'''

def calcularImporteConIVA(importe, iva = 21):
    return((iva/100)*importe + importe)

print(calcularImporteConIVA(100))

'''
Ejercicio 5
Escribir la función máximo, que recibe 2 números por parámetro y 
retorna el mayor. Luego, usando esta función, escriba un programa que pida 10 números 
al usuario por teclado y al finalizar informe el mayor por pantalla.
'''

def max(numero1, numero2):

    if(numero1 > numero2):
        resultado = numero1
    elif(numero1 < numero2):
        resultado = numero2

    return resultado

def mostrarElMayor():
    maximo = int(input('Ingrese el primer numero para tomar como maximo: '))

    for i in range(10):
        numeroAComparar = int(input('Ingrese otro numero para comparar: '))
        maximo = max(maximo, numeroAComparar)

    return maximo

print(mostrarElMayor())

'''
Ejercicio 6
Escribir una función que calcule el área de un círculo y otra que calcule el volumen de
un cilindro usando la primera función.
'''

import math

def calcularAreaCirculo(radio):
    return math.pi * (radio ** 2)

def calcularVolumenCilindro(area, altura):
    return area * altura

print(calcularVolumenCilindro(calcularAreaCirculo(1),1))

'''
Ejercicio 7
Escribir una función que recibe tres números enteros por parámetros, 
calcula el promedio y retorna “APROBADO” si el promedio es mayor o igual a 7 o 
“DESAPROBADO” si es menor.
'''
def calcularAprobacion(primerNota= 1, segundaNota= 1, tercerNota= 1):
    promedio = (primerNota + segundaNota + tercerNota) / 3

    if(promedio >= 7):
        return print('APROBADO')
    else:
      return print('DESAPROBADO')
    
calcularAprobacion(1,10,10)

'''
Ejercicio 8
Escribir una función que recibe dos números enteros mayores que 1, n y m, y 
retorna la potencia n a la m. Resolver con una estructura de control repetitiva, 
NO con el operador potencia de Python
'''
def calcularPotencia(base= 1, exponente= 0):
    resultado = 1
    for i in range (exponente):
      resultado *= base

    return resultado

print(calcularPotencia(7,2))

'''
Ejercicio 9
Escribir una función que dado un tiempo en horas, minutos y segundos retorne 
esa misma cantidad en segundos.
'''
def calcularTiempoEnSegundos(horas= 0, minutos= 0, segundos= 0):
    return (horas*3600) + (minutos*60) + segundos

print(calcularTiempoEnSegundos(1,1,40))

'''
Ejercicio 10
Escribir una función que dado un año, retorne verdadero si es bisiesto y 
falso en caso contrario.

Nota: Los años bisiestos son múltiplos de 4 y no son múltiplos de 100, pero 
los años múltiplos de 400 si son bisiestos. Estos son algunos ejemplos de posibles 
respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 
no es bisiesto
'''
def esAnioBisiesto(anio):
    return (anio % 4 == 0 and not anio % 100 == 0)

print(esAnioBisiesto(2020))
'''
Ejercicio 11
Escribir un programa que pida dos años y escriba cuántos años bisiestos hay entre 
esas dos fechas (incluidos los dos años).
'''
def cantidadDeAniosBisiestosEntre(anioInicio, anioFin):
    cantidad = 0
    for i in range (anioInicio + 1, anioFin):
        if(esAnioBisiesto(i)):
           cantidad += 1

    return cantidad

print(cantidadDeAniosBisiestosEntre(2019,2025))

'''
Ejercicio 12
Escribir una función que tome por parámetro un numero entero y retorne la suma 
de sus dígitos. Para obtener los digitos deben ir dividiendo (division entera) 
por 10 sucesivamente y tomando el resto (digito que esta mas a la derecha).
'''

def sumarDigitos(numero):

    cantidad = 0
    longitud = len(str(numero))

    for i in range (longitud):
        cantidad += numero % 10
        numero = numero // 10

    return cantidad

print(sumarDigitos(127))

'''
Ejercicio 13
Escribir un programa que pida números positivos 
(Debe dejar de pedir números cuando se ingrese uno positivo). 
Mostrar el número cuya sumatoria de dígitos fue mayor y la cantidad de números cuya 
sumatoria de dígitos fue menor que 10. Utilizar una o más funciones, 
según sea necesario.
'''

'''
Ejercicio 14
Escribir un programa que solicita el ingreso de números primos. 
La lectura finalizará cuando ingrese un número que no sea primo. 
Por cada número, mostrar la suma de sus dígitos. Al finalizar el programa, 
mostrar el factorial del mayor número ingresado. Utilizar una o más funciones, 
según sea necesario.
'''