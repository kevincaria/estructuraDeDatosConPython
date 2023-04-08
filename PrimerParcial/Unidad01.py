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

'''
Ejercicio 14
Escribir un programa que pregunte una edad y muestre por pantalla si es mayor de edad o no.
'''
edad = int(input('Ingrese su edad: '))

if edad >= 18:
    print('Sos mayor de edad')
else:
    print('No sos mayor de edad')

'''
Ejercicio 15
Escribir un programa que almacene la cadena de caracteres "contraseña" en una variable y 
luego pregunte por la contraseña e imprima por pantalla si la contraseña introducida en 
la consola coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''
password = 'hola1234'
password_ingresado = input('Ingrese la contraseña: ')

if password == password_ingresado.lower():
    print('Contraseña ingresada correctamente')
else:
    print('Contraseña invalida')

'''
Ejercicio 15b
Escribir un programa pida dos números enteros e informe por pantalla cual es menor de los dos, 
si son iguales, indicarlo por separado.
'''

primer_numero = int(input('Ingrese un numero entero: '))
segundo_numero = int(input('Ingrese un segundo numero entero: '))

if (primer_numero < segundo_numero):
    print('El primer numero es menor')
elif (primer_numero == segundo_numero):
    print('Ambos numeros son iguales')
else:
    print('El segundo numero es menor')

'''
Ejercicio 16
Escribir un programa que pida un número entero e indique si dicho número es par o impar.
'''
numero = int(input('Ingrese un numero: '))

if(numero % 2 == 0):
    print('El numero es par')
else:
    print('El numero es impar')
'''
Ejercicio 17
Para pagar un determinado impuesto se debe ser mayor de 18 años y tener unos ingresos iguales 
o superiores a $100000 mensuales. Escribir un programa que pregunte la edad y 
los ingresos mensuales y muestre por pantalla si se debe pagar o no.
'''
def esMayorDeEdad(edad):
    return(edad>=18)

def tieneIngresosRequeridos(ingreso):
    return(ingreso>=100000)

edad = int(input('Ingrese su edad: '))

ingreso = int(input('Ingrese su ingreso mensual: '))

if(esMayorDeEdad(edad) and tieneIngresosRequeridos(ingreso)):
    print('Debe pagar el impuesto')
else:
    print('No debe pagar el impuesto')

'''
Ejercicio 18
Escribir un programa que pida un número entero del 1 al 7 y muestre por pantalla el día 
de la semana correspondiente. Controlar que el número se encuentre en el rango correcto, 
si no es así, informar un error. Por ejemplo, si el número es 2 el día es martes.
'''
numero = int(input('Ingrese un número entero: '))
semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

if numero == 1:
  print("Domingo")
elif numero ==2:
  print("Lunes")
elif numero == 3:
  print("Martes")
elif numero == 4 :
  print("Miercoles")
elif numero == 5 :
  print("Jueves")
elif numero == 6:
  print("Viernes")
elif numero == 7:
  print("Sabado")
else:
  print("Número incorrecto")

'''
Ejercicio 19
Las y los alumnas y alumnos de un curso se han dividido en dos grupos A y B de acuerdo al género 
y el nombre. 
El grupo A esta formado por las personas de genero femenino con una inicial 
de nombre anterior a la M y las personas de genero masculino con un inicial de nombre posterior 
a la N y 
el grupo B por el resto. 
Escribir un programa que pregunte la inicial y el género, y muestre por pantalla el grupo que corresponde.
'''
genero = input('Ingrese su genero: (Masculino o Femenino): ')
inicial = input('Ingrese la inicial de su nombre: ')

if(genero.capitalize() == 'Femenino' and inicial.upper()<= 'M'):
  print('Pertenece al grupo A')
elif(genero.capitalize() == 'Masculino' and inicial.upper() >= 'N'):
  print('Pertenece al grupo B')
else:
  print('No pertenece a ningun grupo')

'''
Ejercicio 20
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y 
quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
El programa debe preguntar la edad del cliente y mostrar el precio de la entrada. 
Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $5 
y si es mayor de 18 años, $10.
'''
edad = int(input('Ingrese su edad: '))

if(edad < 4):
    print('Entra Gratis !!')
elif(edad >= 4 and edad <= 18):
    print('Debe pagar $5 para entrar')
else:
    print('Debe pagar $10 para entrar')

'''
Ejercicio 21
Mostrar por pantalla todos los números enteros entre 1 y 100, hacerlo usando un bucle while y 
tambien con un bucle for.
'''

numero = 1

while (numero < 101):
    print(numero)
    numero += 1

for i in range(1,101):
    print(i)

'''
Ejercicio 22
Escribir un programa que pida dos números enteros e imprima todos los números enteros entre ellos.
'''
primer_numero = int(input('Ingrese un numero entero: '))
segundo_numero = int(input('Ingrese un segundo numero entero: '))

for i in range(primer_numero + 1, segundo_numero):
    print(i)

'''
Ejercicio 23
Escribir un programa que pregunte un nombre en la consola y un número entero e imprima por 
pantalla en líneas distintas el nombre tantas veces como el número introducido.
'''
nombre = input('Ingrese un nombre: ')
cantidad = int(input('Ingrese un numero para repetir el nombre: '))

for i in range (0,cantidad):
    print(nombre)

'''
Ejercicio 24
Escribir un programa que pida un número entero positivo y muestre por pantalla todos 
los números impares desde 1 hasta ese número.
'''

numero = int(input('Ingrese un numero entero positivo: '))

for i in range (1, numero+1):
    if i % 2 != 0:
        print(i)    

'''
Ejercicio 25
Escribir un programa que pida un número entero y muestre por pantalla un triángulo rectángulo 
como el de más abajo, de altura igual al número introducido.

Por ejemplo, si el usuario ingresa el numero 4:

*

* *

* * *

* * * *

'''
palabra = '*'+' '
cantidad = int(input('Ingrese un numero: '))

while(cantidad > 0):
    print(palabra)
    palabra += '*'+' '
    cantidad -= 1

'''
Ejercicio 26
Escribir un programa que imprima por pantalla todas las fichas del domino, una por línea, 
sin repetir.

0 | 0 - 0 | 1 - 0 | 2 - 0 | 3 - 0 | 4 - 0 | 5 - 0 | 6

1 | 1 - 1 | 2 - 1 | 3 - 1 | 4 - 1 | 5 - 1 | 6

2 | 2 - 2 | 3 - 2 | 4 - 2 | 5 - 2 | 6

3 | 3 - 3 | 4 - 3 | 5 - 3 | 6

4 | 4 - 4 | 5 - 4 | 6

5 | 5 - 5 | 6

6 | 6
'''
[ ]
'''
Ejercicio 27
Escribir un programa que pida un número entero y muestre por pantalla un triángulo rectángulo 
como el de más abajo.

Si el usuario ingresa el numero 5:

1

3 1

5 3 1

7 5 3 1

9 7 5 3 1
'''
[ ]
'''
Ejercicio 28
Escribir un programa que pida un número natural N e imprima por pantalla la suma de los 
números naturales de 1 hasta N.

Por ejemplo para N = 5, la salida debe ser:

1 + 2 + 3 + 4 + 5 = 15
'''
[ ]
'''
Ejercicio 29
Construir un programa que lea un número natural N y calcule la suma de los primeros N números pares.

Si N = 2 -> Resultado = 2 + 4
Si N = 3 -> Resultado = 2 + 4 + 6
Si N = 4 -> Resultado = 2 + 4 + 6 + 8
......
Para cualquier N -> Resultado = 2 + 4 + 6 +....+ 2*N
'''
[ ]
'''
Ejercicio 30
Escribir un programa que pida dos números enteros e informa por pantalla todos los números 
pares entre ellos.
'''
[ ]
'''
Ejercicio 31
Escribir un programa que pida un número entero y muestre por pantalla la cantidad de cifras 
de dicho número. Se debe resolver con divisiones sucesivas por 10 usando un bucle while.
'''
[ ]
'''
Ejercicio 32
Escribir un programa que pida un número entero e informe si dicho numero es primo o compuesto.
'''