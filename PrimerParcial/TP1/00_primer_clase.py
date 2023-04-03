'''
Estructura de datos
Comisión 2
Profesor Martin Pustilnik martin.pustilnik@unahur.edu.ar

Ver videos antes de la clase presencial, nos avisan por mail y/o discord

Lunes presencial 18 a 22 lab 7
Viernes virtual 18 a 22 por meet -> meet.google.com/xiy-avgo-uzg
                                    meet.google.com/tfi-zixo-jby
1er Parcial (15 de Mayo)
    - Tipos de datos abstractos
    - Recursividad
    - Arreglos uni y multidimensionales
    - Pilas y colas

2do Parcial (3 de Julio)
Recuperatorios 10 y 14 de Julio
'''
# TP1
#Primer parte
'''
**Ejercicio 1**
Primer programa en Python. Escribir un programa que imprima por pantalla "Hola mundo".'''
print("Hola mundo")

'''
Ejercicio 2
Escribir un programa que cargue en una variable la cadena de caracteres “Hola mundo” y luego la imprima por pantalla.'''
primer_string = "Hola mundo"
print(primer_string)

'''
Ejercicio 3
Escribir un programa que cree dos variables enteras, le asigne números arbitrarios (cualquiera) 
y muestre por pantalla: la suma, la resta, la multiplicación, 
la división entera y el resto de la división entera.
'''
primer_numero = 10
segundo_numero = 5

print(primer_numero + segundo_numero)
print(primer_numero - segundo_numero)
print(primer_numero * segundo_numero)
print(primer_numero // segundo_numero)
print(primer_numero % segundo_numero)

'''
Ejercicio 4
Implementar algoritmos que permitan:

Calcular el perímetro y el área de un rectángulo, dada su base y su altura
Calcular el perímetro y el área de un círculo dado su radio.
Declarar las variables necesarias y asignarle números arbitrarios
'''

import math
#Rectangulo
base = 10
altura = 5
perimetro = base * 2 + altura * 2
area = base * altura
print('El perimetro de un rectangulo es : ' + str(perimetro))
print('El area de un rectangulo es ' + str(area))
#Circulo
radio = 5
circunferencia = 2 * math.pi * radio
area = (math.pi * radio) ** 2
print(f'La circunferencia de un circulo es: {circunferencia}')
print(f'El area de un circulo es : {area}')

'''
Ejercicio 5
Escribir un programa que pida una temperatura en grados Celsius al usuario, 
realice la transformación de grados Celsius a Fahrenheit e imprima el resultado por pantalla.
'''

temperatura_celsius = float(input('Ingrese una temperatura: '))
temperatura_fahrenheit = temperatura_celsius *1.8 + 32
print(f'Temperatura en fahrenheit es: {temperatura_fahrenheit}ºF')

'''
Ejercicio 6
Escribir un programa que pregunte por el número de horas trabajadas y el costo por hora. 
Después debe mostrar por pantalla el sueldo que corresponde.
'''
horas_trabajadas = float(input('Ingrese la cantidad de horas trabajadas: '))
costo = float(input('Ingrese la cuanto cuesta una hora trabajada: '))
print(f'Su sueldo es de: $ {horas_trabajadas*costo}')

'''
Ejercicio 7
Escribir un programa que pida un peso (en kg) y una estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable. 
Luego debe muestrar por pantalla la frase: "El índice de masa corporal es: <imc>". 
Donde <imc> es el índice de masa corporal calculado.
'''

peso = float(input('Ingrese su peso: '))
estatura = float(input('Ingrese su estatura: '))
imc = peso*(estatura**2)
print(f'Su IMC es: {imc}')

'''
Ejercicio 8
Escribir un programa que pregunte una cantidad a invertir, el interés anual y el número de años, 
y muestre por pantalla el capital obtenido en la inversión.
'''

cantidad = float(input('Ingrse la cantidad que quiere invertir: '))
interes = float(input('Ingrese el interes anual: '))
años = float(input('Ingrese la cantidad de años: '))
capital_obtenido = cantidad + ((cantidad*interes)/100)*años
print(f'El capital obtenido en la inversion es de: ${capital_obtenido} ')

'''
Ejercicio 9
Escribir un programa que pregunte un nombre completo en la consola y 
después muestre por pantalla ese nombre tres veces, una con todas las letras minúsculas, 
otra con todas las letras mayúsculas y otra solo con la primera letra del nombre 
y de los apellidos en mayúscula. 
Se puede introducir un nombre combinando mayúsculas y minúsculas como se quiera.
'''

nombre = str(input('Ingrese su nombre:'))
apellido = str(input('Ingrese su apellido: '))
print(f'{nombre.upper()} {apellido.upper()}')
print(f'{nombre.lower()} {apellido.lower()}')
print(f'{nombre.capitalize()} {apellido.capitalize()}')

'''
Ejercicio 10
Escribir un programa que pregunte un nombre en la consola y después muestre por pantalla: 
"El <NOMBRE> tiene <N> letras", donde <NOMBRE> es el nombre ingresado todo en mayúsculas y 
<N> es el número de letras que tienen el nombre.
'''

nombre = str(input('Ingrese su nombre:'))
print(f'La palabra {nombre} tiene {len(nombre)} letras')

'''
Ejercicio 11
Escribir un programa que pida una palabra, reemplace todas las letras "a" por "z" y 
muestre el resultado por pantalla.
'''

palabra = str(input('Ingrese su palabra:'))
palabra_cambiada = ''
for letra in palabra:
    if letra == 'a':
        palabra_cambiada += 'z'
    else:
        palabra_cambiada += letra

print(palabra_cambiada)

'''Ejercicio 12
Escribir un programa que pida dos palabras y muestre por pantalla la concatenacion de ambas.
'''
primer_palabra = input('Ingrese la primer palabra: ')
segunda_palabra = input('Ingrese la segunda palabra: ')
print(primer_palabra+segunda_palabra)

'''Ejercicio 13
Escribir un programa que pida una palabra y un número N y muestre por pantalla la palabra 
ingresada repetida N veces.
'''
palabra = (input('Ingrese una palabra: ')+' ')
cantidad = int(input('Ingrese la cantidad de veces que quiere que se repita la palabra: '))

print(palabra*cantidad)
