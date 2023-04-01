#Segunda parte: Estructuras de control
'''
Ejercicio 14
Escribir un programa que pregunte una edad y muestre por pantalla si es mayor de edad o no.
'''
# edad = int(input('Ingrese su edad: '))

# if edad >= 18:
#     print('Sos mayor de edad')
# else:
#     print('No sos mayor de edad')

'''
Ejercicio 15
Escribir un programa que almacene la cadena de caracteres "contraseña" en una variable y 
luego pregunte por la contraseña e imprima por pantalla si la contraseña introducida en 
la consola coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''
# password = 'hola1234'
# password_ingresado = input('Ingrese la contraseña: ')

# if password == password_ingresado.lower():
#     print('Contraseña ingresada correctamente')
# else:
#     print('Contraseña invalida')

'''
Ejercicio 15b
Escribir un programa pida dos números enteros e informe por pantalla cual es menor de los dos, 
si son iguales, indicarlo por separado.
'''

# primer_numero = int(input('Ingrese un numero entero: '))
# segundo_numero = int(input('Ingrese un segundo numero entero: '))

# if (primer_numero < segundo_numero):
#     print('El primer numero es menor')
# elif (primer_numero == segundo_numero):
#     print('Ambos numeros son iguales')
# else:
#     print('El segundo numero es menor')

'''
Ejercicio 16
Escribir un programa que pida un número entero e indique si dicho número es par o impar.
'''
# numero = int(input('Ingrese un numero: '))

# if(numero % 2 == 0):
#     print('El numero es par')
# else:
#     print('El numero es impar')
'''
Ejercicio 17
Para pagar un determinado impuesto se debe ser mayor de 18 años y tener unos ingresos iguales 
o superiores a $100000 mensuales. Escribir un programa que pregunte la edad y 
los ingresos mensuales y muestre por pantalla si se debe pagar o no.
'''
# def esMayorDeEdad(edad):
#     return(edad>=18)

# def tieneIngresosRequeridos(ingreso):
#     return(ingreso>=100000)

# edad = int(input('Ingrese su edad: '))

# ingreso = int(input('Ingrese su ingreso mensual: '))

# if(esMayorDeEdad(edad) and tieneIngresosRequeridos(ingreso)):
#     print('Debe pagar el impuesto')
# else:
#     print('No debe pagar el impuesto')

'''
Ejercicio 18
Escribir un programa que pida un número entero del 1 al 7 y muestre por pantalla el día 
de la semana correspondiente. Controlar que el número se encuentre en el rango correcto, 
si no es así, informar un error. Por ejemplo, si el número es 2 el día es martes.
'''
# numero = int(input('Ingrese un número entero: '))
# semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

# if numero == 1:
#   print("Domingo")
# elif numero ==2:
#   print("Lunes")
# elif numero == 3:
#   print("Martes")
# elif numero == 4 :
#   print("Miercoles")
# elif numero == 5 :
#   print("Jueves")
# elif numero == 6:
#   print("Viernes")
# elif numero == 7:
#   print("Sabado")
# else:
#   print("Número incorrecto")

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
# genero = input('Ingrese su genero: (Masculino o Femenino): ')
# inicial = input('Ingrese la inicial de su nombre: ')

# if(genero.capitalize() == 'Femenino' and inicial.upper()<= 'M'):
#   print('Pertenece al grupo A')
# elif(genero.capitalize() == 'Masculino' and inicial.upper() >= 'N'):
#   print('Pertenece al grupo B')
# else:
#   print('No pertenece a ningun grupo')

'''
Ejercicio 20
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y 
quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
El programa debe preguntar la edad del cliente y mostrar el precio de la entrada. 
Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $5 
y si es mayor de 18 años, $10.
'''
# edad = int(input('Ingrese su edad: '))

# if(edad < 4):
#     print('Entra Gratis !!')
# elif(edad >= 4 and edad <= 18):
#     print('Debe pagar $5 para entrar')
# else:
#     print('Debe pagar $10 para entrar')

'''
Ejercicio 21
Mostrar por pantalla todos los números enteros entre 1 y 100, hacerlo usando un bucle while y 
tambien con un bucle for.
'''

# numero = 1

# while (numero < 101):
#     print(numero)
#     numero += 1

# for i in range(1,101):
#     print(i)

'''
Ejercicio 22
Escribir un programa que pida dos números enteros e imprima todos los números enteros entre ellos.
'''
# primer_numero = int(input('Ingrese un numero entero: '))
# segundo_numero = int(input('Ingrese un segundo numero entero: '))

# for i in range(primer_numero + 1, segundo_numero):
#     print(i)

'''
Ejercicio 23
Escribir un programa que pregunte un nombre en la consola y un número entero e imprima por 
pantalla en líneas distintas el nombre tantas veces como el número introducido.
'''
# nombre = input('Ingrese un nombre: ')
# cantidad = int(input('Ingrese un numero para repetir el nombre: '))

# for i in range (0,cantidad):
#     print(nombre)

'''
Ejercicio 24
Escribir un programa que pida un número entero positivo y muestre por pantalla todos 
los números impares desde 1 hasta ese número.
'''

# numero = int(input('Ingrese un numero entero positivo: '))

# for i in range (1, numero+1):
#     if i % 2 != 0:
#         print(i)    

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
# palabra = '*'+' '
# cantidad = int(input('Ingrese un numero: '))

# while(cantidad > 0):
#     print(palabra)
#     palabra += '*'+' '
#     cantidad -= 1

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