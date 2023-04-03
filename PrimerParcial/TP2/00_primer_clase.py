
'''
Ejercicio 3
Escribir   una   función   que   calcule   y   retorne   el   factorial   de   un   numero   natural.
'''

# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result = result * i
#     return result

# print(factorial(3))

'''
Ejercicio 4
Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función
debe recibir el importe sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la
factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un
21%.'''

# def calcularImporteConIVA(importe, iva = 21):
#     return((iva/100)*importe + importe)

# print(calcularImporteConIVA(100))

'''
Ejercicio 5
'''

# def max(numero1, numero2):

#     if(numero1 > numero2):
#         resultado = numero1
#     elif(numero1 < numero2):
#         resultado = numero2

#     return resultado

# def mostrarElMayor():
#     maximo = int(input('Ingrese el primer numero para tomar como maximo: '))

#     for i in range(10):
#         numeroAComparar = int(input('Ingrese otro numero para comparar: '))
#         maximo = max(maximo, numeroAComparar)

#     return maximo

# print(mostrarElMayor())

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

#Hacer hasta el 12
digito = numero % 10
print(digito)
numero = numero // 10
digito = numero % 10
print(digito)