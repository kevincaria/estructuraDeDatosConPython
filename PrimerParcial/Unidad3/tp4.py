import numpy as np
# Ejercicio 1
# Escribir un programa que le pida al usuario que ingrese 10 números 
# enteros (primero uno, luego otro, y así hasta que el usuario ingrese 10 numeros). 
# Al final, el programa debe imprimir los números que fueron ingresados en orden inverso, 
# la suma total de los valores y el promedio.
def pedirNumeros():
    vector = np.zeros(10,int)

    for i in range(len(vector)):
        vector[i] = int(input(f'Ingrese un numero para la posicion {str(i)}:'))

    print(vector)

# Ejercicio 2
# Escribir una función que recibe un arreglo de enteros por parámetro y lo retorna con 
# el contenido desplazado una posición hacia la derecha: el primero pasa a ser el segundo, 
# el segundo pasa a ser el tercero y así sucesivamente. El último pasa a ser el primero.

# Luego, escribir un programa que cargue un arreglo con valores ingresados por el usuario y 
# llame a la función con ese arreglo. Mostrar el contenido del arreglo por pantalla, antes 
# y después de la función.

# Por ejemplo:
# Arreglo original = [2, 4, 1, 5, 7, 9]
# Arreglo desplazado = [9, 2, 4, 1, 5, 7]

vector = np.array([2, 4, 1, 2, 7, 9])

def desplazarNumeros(vector):
    vectorDesplazado = np.zeros(len(vector),int)
    for i in range(len(vector)):
        if i == len(vector)-1:
            vectorDesplazado[0] = vector[i]
        else:
            vectorDesplazado[i + 1] = vector[i]

    for i in range(len(vector)):
        vector[i] = vectorDesplazado[i]

def desplazarNumerosProfe(vector):
    for indice in reversed(range(len(vector)-1)):
        aux = vector[indice]
        vector[indice] = vector[indice + 1]
        vector [indice + 1] = aux
    
def desplazarNumerosEn1Linea(vector):
    for indice in reversed(range(len(vector)-1)):
        vector[[indice, indice + 1]] = vector[[indice + 1, indice]]

# Ejercicio 3
# Desarrollar una función que inserte un elemento en un arreglo de enteros dada 
# la posición de inserción. Al insertar un elemento en una posición,
# se produce un desplazamiento a la derecha, si el arreglo estaba lleno, 
# el último elemento se pierde.

# Por ejemplo:

# Si insertamos el elemento 5 en la posicion 3 del arreglo:
# Arreglo antes de insertar = [2, 4, 1, 7, 6, 2]
# Arreglo despues de insertar = [2, 4, 1, 5, 7, 6]
def insertarNumero(vector,posicion,numero):
    for i in reversed(range(posicion +1, len(vector))):
        vector[i]= vector[i-1]
    vector[posicion] = numero
    return vector
# Ejercicio 4
# Escribir una función que elimine el elemento que ocupa una determinada posición 
# de un arreglo de enteros. Al eliminar se debe mantener la continuidad, es decir, 
# los elementos a la derecha del eliminado, deben desplazarse a la izquierda un lugar.

# Por ejemplo:

# Si eliminamos el elemento de la posicion 2 del arreglo:

# Arreglo antes de eliminar = [4, 3, 5, 8, 6, 7]

# Arreglo despues de eliminar = [4, 3, 8, 6, 7, 0]
def eliminarNumero(vector,posicion):
    for i in (range(posicion+1,len(vector))):
        vector[i-1] = vector[i]

    vector[len(vector)-1] = 0
    return vector

# Ejercicio 5
# Escribir una función que elimine todas las apariciones de un determinado 
# elemento de un arreglo de enteros.
def eliminarRepetido(vector,numero):
    for i in range(len(vector)):
        if vector[i] == numero:
            vector[i] = 0
    return vector


# Ejercicio 6
# Escribir una función recursiva que reciba un arreglo de números reales como parámetro 
# y retorne la suma de todos los elementos del arreglo.

def sumaVector(vector, indice):
    suma = 0
    if indice == 0:
        suma += vector[indice] 
    else:
        suma += vector[indice] + sumaVector(vector, indice-1)

    return suma

# Ejercicio 7
# Escribir un programa que crea y cargar dos matrices de tamaño 3x3, las suma 
# y muestra el resultado.
primerMatriz = np.array([[1 , 2 , 3] ,[2 , 5 , 0],[3 , 0 , 9]])
segundaMatriz = np.array([[1 , 2 , 2] ,[1 , 1 , 2], [1 , 1 , 1]])
def sumarMatriz(primerMatriz, segundaMatriz):
    matrizSumada = np.zeros((3,3),int)
    for i in range(len(primerMatriz)):
        for j in range(len(primerMatriz[i])):
            matrizSumada[i][j] = primerMatriz[i][j] + segundaMatriz[i][j]
    return matrizSumada

# Ejercicio 8
# Escribir una función que recibe una matriz y la rellena de la siguiente forma: 
# En la posición M[ i , j ] debe contener i + j.
def sumarPosiciones():
    matrizSumada = np.zeros((3,3),int)
    for i in range(len(matrizSumada)):
        for j in range(len(matrizSumada[i])):
            matrizSumada[i][j] = i + j
    return matrizSumada

# Ejercicio 9
# Desarrollar una función que recibe una matriz cuadrada de números reales (N x N) 
# por parámetro y calcula la suma de los elementos que están por encima de 
# la diagonal principal (excluyendo la diagonal).

# En el ejemplo de la imagen, la función deberia retornar: b + c + f

def ejercicio9(matriz):
    suma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i < j:
                suma += matriz[i][j]

    return suma

# Ejercicio 10
# Escribir una función que retorna True si una matriz cuadrada de enteros es matriz diagonal 
# y False en caso contrario.

# Una matriz diagonal es una matriz que tiene ceros en todos sus elementos, 
# menos en la diagonal principal.

def esMatrizDiagonal(matriz):
    resultado = False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if (i == j and matriz[i,j] != 0) or (i != j and matriz[i,j] == 0) :
                    resultado = True
            else: 
                resultado = False
                break
    
    return resultado

# Ejercicio 11
# Escribir una función que retorna True si una matriz cuadrada de enteros es simétrica 
# y False en caso contrario.

# Una matriz simétrica es como la de la imagen (no importan los elementos 
# de la diagonal principal):

# texto alternativo

def ejercicio11(matriz):
    resultado = False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i != j:
                if matriz[i,j] == matriz[j,i]:
                    resultado = True
                else: 
                    resultado = False
                    break
    return resultado

print(ejercicio11(primerMatriz))
# Ejercicio 12
# Escribir una función recursiva, que calcule la suma de los elementos 
# de la diagonal principal de una matriz.

# Nota: La suma de los elementos de la diagonal principal de una matriz 
# se llama "traza de la matriz".


# Comentario
# En los ejercicios que usan cadenas de caracteres, pueden usar el tipo str, 
# salvo que necesiten modificar elementos de la cadena luego de crearla, en ese caso, 
# tienen que usar arreglos de caracteres.

# Ejercicio 13
# Escribir 3 procedimientos que reciben una cadena de caracteres y..:

# Imprima los dos primeros caracteres.
# Imprima los tres últimos caracteres.
# Imprima la cadena cada dos caracteres. Por ej.: 'recta' debería imprimir 'rca'


# Ejercicio 14
# Desarrollar una función recursiva que retorna True si una cadena de caracteres 
# es un palíndromo y False en caso contrario.

# Nota: Palíndromo es la forma elegante de "capicua"


# Ejercicio 15
# Escribir una función que recibe una cadena de caracteres y un caracter y 
# retorna una nueva cadena que tiene el caracter entre cada letra de la cadena de entrada.

# Por ej si la cadena es: ' separar ' y el caracter es: ' , ', 
# debería retornar ' s,e,p,a,r,a,r '


# Ejercicio 16
# Escribir una función que recibe un arreglo variables de tipo "Tiempo" 
# (TDA del ejercicio 4 del TP de TDA) y retorna un nuevo arreglo solo 
# con los tiempos que son mayores a una hora (1:00:00).

# Escribir un programa para probar a la función.

# Nota: Van a tener que copiar el TDA "Tiempo" en el bloque de código de abajo 
# y para que un print de un vector de variables de tipo "Tiempo" funcione, tienen que programar la operacion "__repr__()" en el TDA "Tiempo".