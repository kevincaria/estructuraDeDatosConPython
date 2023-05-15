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

def sumaVectorProfe(vector):
    resultado = vector[0] #Caso base de la recursion sin if
    if len(vector)>0:
        resultado = resultado + sumaVectorProfe(vector[1:])
    return resultado

# Ejercicio 7
# Escribir un programa que crea y cargar dos matrices de tamaño 3x3, las suma 
# y muestra el resultado.
primerMatriz = np.array([[1 , 2 , 3] ,[2 , 5 , 0],[3 , 0 , 9]])
segundaMatriz = np.array([[1 , 0 , 0] ,[0 , 1 , 0], [0 , 0 , 1]])
def sumarMatriz(primerMatriz, segundaMatriz):
    matrizSumada = np.zeros((3,3),int)
    for i in range(len(primerMatriz)):
        for j in range(len(primerMatriz[i])):
            matrizSumada[i][j] = primerMatriz[i][j] + segundaMatriz[i][j]
    return matrizSumada

# Ejercicio 8
# Escribir una función que recibe una matriz y la rellena de la siguiente forma: 
# En la posición M[ i , j ] debe contener i + j.
matrizARellenar = np.zeros((3,3),int)

def sumarPosiciones(matrizARellenar):
    for i in range(len(matrizARellenar)):
        for j in range(len(matrizARellenar[i])):
            matrizARellenar[i][j] = i + j

# Ejercicio 9
# Desarrollar una función que recibe una matriz cuadrada de números reales (N x N) 
# por parámetro y calcula la suma de los elementos que están por encima de 
# la diagonal principal (excluyendo la diagonal).

# En el ejemplo de la imagen, la función deberia retornar: b + c + f

def sumaSobreDiagonal(matriz):
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
    resultado = True
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if not((i == j and matriz[i,j] != 0) or (i != j and matriz[i,j] == 0)) :
                    resultado = False
    
    return resultado

# Ejercicio 11
# Escribir una función que retorna True si una matriz cuadrada de enteros es simétrica 
# y False en caso contrario.

# Una matriz simétrica es como la de la imagen (no importan los elementos 
# de la diagonal principal):

# texto alternativo

def esSimetrica(matriz):
    resultado = True
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i != j:
                if matriz[i,j] != matriz[j,i]:
                    resultado = False
    return resultado

# Ejercicio 12
# Escribir una función recursiva, que calcule la suma de los elementos 
# de la diagonal principal de una matriz.

# Nota: La suma de los elementos de la diagonal principal de una matriz 
# se llama "traza de la matriz".

# Comentario
# En los ejercicios que usan cadenas de caracteres, pueden usar el tipo str, 
# salvo que necesiten modificar elementos de la cadena luego de crearla, en ese caso, 
# tienen que usar arreglos de caracteres.
def sumarDiagonal(matriz, indice):
    resultado = 0
    if indice == 0:
        resultado += matriz[indice, indice] 
    else:
        resultado += matriz[indice, indice] + sumarDiagonal(matriz, indice-1)

    return resultado

# Ejercicio 13
# Escribir 3 procedimientos que reciben una cadena de caracteres y..:

# Imprima los dos primeros caracteres.
# Imprima los tres últimos caracteres.
# Imprima la cadena cada dos caracteres. Por ej.: 'recta' debería imprimir 'rca'
arreglo = np.array(['p', 'y', 't', 'h', 'o', 'n'])

arreglo2 = np.array(['p', 't', 't', 't', 't', 'p'])


def imprimirDosPrimeros(arreglo):
    return print(arreglo[0]+arreglo[1])

def imprimirTresUltimos(arreglo):
    return print(arreglo[-3]+arreglo[-2]+arreglo[-1])

def imprimirCadaDos(arreglo):
    resultado = ''
    for indice in range(0,len(arreglo),2):
        resultado += arreglo[indice]
    return print(resultado)

imprimirCadaDos(arreglo)
# Ejercicio 14
# Desarrollar una función recursiva que retorna True si una cadena de caracteres 
# es un palíndromo y False en caso contrario.

# Nota: Palíndromo es la forma elegante de "capicua"

def esPalindromo(arreglo, inicio, final):
    resultado = True
    if inicio >= final:
        resultado = True
    else:
        resultado = arreglo[inicio] == arreglo[final] and esPalindromo(arreglo, inicio + 1, final -1)

    return resultado

# Ejercicio 15
# Escribir una función que recibe una cadena de caracteres y un caracter y 
# retorna una nueva cadena que tiene el caracter entre cada letra de la cadena de entrada.

# Por ej si la cadena es: ' separar ' y el caracter es: ' , ', 
# debería retornar ' s,e,p,a,r,a,r '

def arregloConCaracterNuevo(arreglo,caracter):
    arregloNuevo = np.empty((len(arreglo)*2,), dtype=str)

    for i in range(len(arreglo)):
        arregloNuevo[i*2] = arreglo[i]
        arregloNuevo[i*2+1] = caracter

    return arregloNuevo

def arregloConCaracter(arreglo,caracter):
    arregloNuevo = np.empty((len(arreglo)*2-1,), dtype=str)

    for i in range(len(arregloNuevo)):
        if i%2==0:
            arregloNuevo[i]=arreglo[i//2]
        else:
            arregloNuevo[i] = caracter

    return arregloNuevo

# Ejercicio 16
# Escribir una función que recibe un arreglo variables de tipo "Tiempo" 
# (TDA del ejercicio 4 del TP de TDA) y retorna un nuevo arreglo solo 
# con los tiempos que son mayores a una hora (1:00:00).

# Escribir un programa para probar a la función.

# Nota: Van a tener que copiar el TDA "Tiempo" en el bloque de código de abajo 
# y para que un print de un vector de variables de tipo "Tiempo" funcione, tienen que programar la operacion "__repr__()" en el TDA "Tiempo".
import Unidad2.tp2 as tp2

t1 = tp2.Tiempo(1, 20, 30)
t2 = tp2.Tiempo(2, 45, 15)
t3 = tp2.Tiempo(0, 15, 0)

vectorTiempos = np.array([t1, t2, t3])

def tiemposMayorAUnaHora(vectorTiempos:np.ndarray[tp2.Tiempo]):
    hora = tp2.Tiempo(1,0,0)
    horasConMasDeUnaHora = np.empty((len(vectorTiempos),), dtype=tp2.Tiempo)
    indiceNuevo = 0
    for i in range(len(vectorTiempos)):
        if vectorTiempos[i].tiempoASegundos() > hora.tiempoASegundos():
            horasConMasDeUnaHora[indiceNuevo] = vectorTiempos[i]
            indiceNuevo +=1

    return horasConMasDeUnaHora

# Ejercicio extra
# hacer una funcion recursiva que reciba un arreglo y retorne el minimo
def minimoVector(vector, indice):
    if indice == 0:
        return vector[indice]
    else:
        valor_actual = vector[indice]
        valor_minimo_anterior = minimoVector(vector, indice - 1)
        if valor_actual < valor_minimo_anterior:
            return valor_actual
        else:
            return valor_minimo_anterior

def minimoVectorProfe(vector):
    if len(vector) == 1:
        return vector[0]
    else:
        return min(vector[0], minimoVectorProfe(vector[1:])) #Usando funcion min y [1:]