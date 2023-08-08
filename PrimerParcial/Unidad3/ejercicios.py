# Escribir una función que recibe una lista de números como parámetro y devuelve un diccionario con los números de la lista como claves y la cantidad de apariciones de cada uno como su significado.

# Por ejemplo:

# Lista de entrada = [1 , 3 , 4 , 2 , 1 , 3 , 1 , 4 , 2 , 5 , 2]

# Diccionario de salida = { (1 , 3) , (3 , 2) , (4 , 2) , (2 , 3) , (5 , 1) }

def contarApariciones(lista):
    diccionario = {}

    for key in lista:
        if key in diccionario:
            diccionario[key] += 1
        else:
            diccionario[key] = 1

    return diccionario

lista = [1, 1, 1, 2, 1, 3, 1, 4, 2, 5, 2]
resultado = contarApariciones(lista)
print(resultado)

# Escribir una función que recibe dos diccionarios y devuelve otro con la mezcla de los dos, para las claves repetidas, se queda con los significados de primer diccionario.

# Por ejemplo:

# Diccionario de entrada 1 = { (1 , 3) , (3 , 2) , (4 , 4) , (2 , 3) , (5 , 1) }

# Diccionario de entrada 2 = { (10 , 3) , (3 , 5) , (2 , 30) , (8 , 1) , (9 , 3) }

# Diccionario de salida = { (1 , 3) , (3 , 2) , (4 , 4) , (2 , 3) , (5 , 1) , (10 , 3) , (8 , 1) , (9 , 3) }

def mezclarDiccionarios(dic1, dic2):
    diccionario = dic1.copy()

    for key in dic2.keys():
        if key not in diccionario:
            diccionario[key] = dic2[key]

    return diccionario

dic1 = {1: 3, 3: 2, 4: 4, 2: 3, 5: 1}
dic2 = {10: 3, 3: 5, 2: 30, 8: 1, 9: 3}

resultado = mezclarDiccionarios(dic1, dic2)
print(resultado)


# Escribir una funcion recursiva que reciba un arreglo y retorne el minimo
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
        
vector = [3, 8, 4, 10, 5]
indiceInicial = len(vector) - 1
resultado = minimoVector(vector, indiceInicial)
print(resultado)

#Escribir una función recursiva que retorna True si una cadena de caracteres 
# es un palíndromo y False en caso contrario.
def esPalindromo(arreglo, inicio, final):
    resultado = True
    if inicio >= final:
        resultado = True
    else:
        resultado = arreglo[inicio] == arreglo[final] and esPalindromo(arreglo, inicio + 1, final -1)

    return resultado

cadena1 = "reconocer"
cadena2 = "oso"
cadena3 = "python"

print(esPalindromo(cadena1, 0, len(cadena1) - 1))  # True
print(esPalindromo(cadena2, 0, len(cadena2) - 1))  # True
print(esPalindromo(cadena3, 0, len(cadena3) - 1))  # False

# Escribir una función recursiva que reciba un arreglo de números reales como parámetro 
# y retorne la suma de todos los elementos del arreglo.
def sumaVector(vector, indice):
    if indice == 0:
        return vector[indice]
    else:
        return vector[indice] + sumaVector(vector, indice - 1)

vector = [1.5, 2.0, 3.5, 4.0, 5.5]
indiceInicial = len(vector) - 1
resultado = sumaVector(vector, indiceInicial)
print(resultado)


# Desarrollar una función que recibe una matriz cuadrada de números reales (N x N) 
# por parámetro y calcula la suma de los elementos que están por encima de 
# la diagonal principal (excluyendo la diagonal).

def sumaSobreDiagonal(matriz):
    suma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i < j:
                suma += matriz[i][j]

    return suma

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado = sumaSobreDiagonal(matriz)
print(resultado)

# Escribir una función que elimine todas las apariciones de un determinado 
# elemento de un arreglo de enteros.
def eliminarRepetido(vector, numero):
    vector_filtrado = []
    for elemento in vector:
        if elemento != numero:
            vector_filtrado.append(elemento)
    return vector_filtrado

vector = [1, 2, 3, 2, 4, 2, 5]
resultado = eliminarRepetido(vector, 2)
print(resultado)
