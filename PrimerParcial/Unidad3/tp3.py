# Ejercicio 1
# Implementar una función que calcule el factorial de un número de forma recursiva

# Ejercicio 2
# Una canilla de una casa pierde agua de forma que todos los días pierde 2 gotas más que el día anterior. Escribir una función recursiva que calcule cuantas gotas perderá la canilla el día N. El primer día solo perdía dos gotas.

# Ejercicio 3
# Implementar una función recursiva que calcule los números de la serie de Fibonacci. La función para generar la serie de Fibonacci es la siguiente (donde N es el índice del número en la serie):

# alt text

# Luego escribir un programa que pida un número N (mayor o igual a 0) al usuario e imprima por pantalla los primeros N números de la serie de Fibonacci

# Sobre la sucesion de Fibonacci: https://www.vix.com/es/btg/curiosidades/4461/que-es-la-sucesion-de-fibonacci



# Ejercicio 4
# Escribir una función recursiva que calcule el número triangular de índice N. El número triangular de índice N es la suma de todos los números desde 1 hasta N.

# Algunos ejemplos:

# T(1) = 1

# T(2) = 1 + 2

# T(3) = 1 + 2 + 3

# T(4) = 1 + 2 + 3 + 4

# T(5) = 1 + 2 + 3 + 4 + 5

# ...

# T(N) = 1 + 2 + 3 + 4 + ... + N



# Ejercicio 5
# En las redes sociales se produce una continua interacción y cada vez que un usuario realiza una acción, la comunidad se modifica. Suponiendo que un influencer que usa Instagram cada vez que postea algo, aumenta su cantidad de seguidores según la siguiente regla:

# Durante los primeros 20 posteos, siempre suma una cantidad fija de 1000 (mil) seguidores en cada uno.
# A partir del posteo 21, la cantidad de seguidores duplica la cantidad previa de seguidores, mas 500 seguidores extra.
# Implementar una función recursiva que permita saber cuantos seguidores tendra el Instagramer luego de una cantidad determinada de posteos.


# Ejercicio 6
# Un equipo de albañiles de una obra, tiene que planificar la colocación de pisos. Dicha tarea se realiza teniendo algunas consideraciones específicas, que tienen que ver con el corte de las baldosas, con el material de pegado y la cantidad de trabajadores que hay en cada momento. En el arranque, el día uno (1), los albañiles colocan siempre 100 baldosas. Luego, la cantidad que se coloca cada día se organiza de esta manera:

# Los días pares se colocan el doble de baldosas del día anterior.
# Los días impares (salvo el primer día) se coloca una cantidad igual a la suma de las que se colocaron los 2 dias anteriores.
# Implementar una función que permita saber la cantidad de baldosas que se colocan en total luego de transcurrida una determinada cantidad de días.



# Ejercicio 7
# Luego de una lluvia muy grande se acumula gran cantidad de agua en un estanque, durante el primer día, el agua comienza a ponerse de color verde y un grupo de científicos decide medir cuantas algas encuentra dentro del tanque. La primer medición le da como resultado 12 algas. Luego deciden ir a realizar la medición todos los días para tratar de establecer un patrón de crecimiento y se encuentran que las algas crecen con la siguiente regla:

# Durante los siguientes 10 días (del dia 2 al 11) la cantidad de algas en el tanque es 15 más de las que había el día anterior.
# A partir del día 12, la cantidad de algas en el tanque es el triple de las que había el día previo más una cantidad fija de 100.
# Escriba una función recursiva que calcule la cantidad de algas en el tanque en un día N.

# Nota: Suponer que no mueren algas en el tanque.



# Ejercicio 8
# Escribir una función recursiva que calcule la potencia N de un número M (M a la N), ambos números enteros positivos.



# Ejercicio 9
# Problema del trigo en el tablero de ajedrez:

# alt text

# Si se colocase sobre un tablero de ajedrez, un grano de trigo en el primer casillero, dos en el segundo, cuarto en el tercero y asi sucesivamente, doblando la cantidad de granos en cada casilla ¿Cuantos granos de trigo habría en el tablero en total al final? Resolver el problema con una función recursiva.

# Leyenda del Trigo y el tablero de ajedrez y mas datos: https://matematicascercanas.com/2014/03/10/la-leyenda-del-tablero-de-ajedrez-y-los-granos-de-trigo/



# Ejercicio 10
# En un edificio alto, las cucarachas se van distribuyendo por pisos de esta forma:

# En el primer piso hay una cucaracha
# En los pisos pares el doble del número de piso (por ejemplo en el piso 8 hay 16 cucarachas)
# El resto de los pisos tienen la suma de las cucarachas de los dos pisos anteriores.
# Escribir una función recursiva que calcule la cantidad de cucarachas en un edificio en función de la cantidad de pisos.



# Ejercicio 11
# Escribir la función recursiva repetirPalabra, que recibe como parámetro una palabra (cadena de caracteres) y un número N. La función debe retornar una nueva cadena que contenga la palabra repetida N veces, por ejemplo:

# repetirPalabra("hola",3) -> "holaholahola"



# Ejercicio 12
# Escribir una función recursiva que calcule el número combinatorio, es decir, las combinaciones de N elementos tomados de a M, usando la siguiente expresión:

# numeroCombiantorio.png



# Ejercicio 13
# Juan y María empiezan a trabajar el mismo día en dos empresas distintas. Juan arregla un sueldo inicial de $40000 con una actualización mensual del 2% y María un sueldo inicial de $25000 con una actualización mensual del 5%. Calcular recursivamente los sueldos de Juan y de María luego de transcurridos una cantidad determinada de meses.

# Luego, escribir un programa que calcule y muestre por pantalla cuantos meses tienen que pasar para que el sueldo de María supere al de Juan (Esta parte no hace falta que sea recursiva, pero pueden intentar hacerlo).