# Ejercicio 1
# Implementar el TDA Diccionario (Map), con las siguientes operaciones (Solo lo tienen que usar, ya esta implementado por nosotros, pero repasen el funcionamiento):

# Crear (__init__()).
# __repr__(): Para poder imprimir por consola.
# insertar(clave, significado): Inserta el par <clave , significado>, si la clave ya existe no debe modificar el diccionario.
# Asignación con "dicc[clave] = significado": Permite modificar significados de claves existentes y agregar nuevos pares. Esto se realiza implementado la función __setitem__().
# get(clave): Recibe una clave y retorna su significado, si la clave no existe lanza una excepción.
# Obtener con "dicc[clave]": Similar a get, pero con el operador "[ ]". Esto se realiza implementando la función __getitem__().
# len(): Retorna la cantidad de pares <clave , significado> en el diccionario.
# getKeys(): Retorna lista con claves.
# getValues(): Retorna lista con significados.
# Operador "in": Permite la búsqueda dentro del diccionario por las claves, es decir podemos hacer "if clave in diccionario".
# remove(clave): Elimina el par clave-significado que contiene la clave que recibe como parámetro
# clone(): Genera nuevo diccionario con el mismo contenido
# clear(): Vacia diccionario
# Si quieren iterar el diccionario deben hacer (por ejemplo para imprimir todos los pares clave-significado en diferentes lineas):

# for clave in diccionario.keys():
#     print(clave, diccionario.get(clave))
# O el equivalente con el operador "[ ]":

# for clave in diccionario.keys():
#     print(clave, dicionario[clave])
# Aunque tengamos el operador "in" este sirve solo para búsquedas y no para iterar en diccionario, entonces no se puede hacer:

# for clave in diccionario:
# [ ]
import copy as cp

class Diccionario:
  #######TDA tupla clave-valor#########################
  class __TuplaDic:
    def __init__(self, key, value):
      self.data = (key,value)

    def __repr__(self):
      return str(self.data)

    def __eq__(self, key):
      return self.data[0] == key

    def __hash__(self):
      return hash(self.data[0])

    def getKey(self):
      return self.data[0]

    def getValue(self):
      return self.data[1]
  #######################################################
  
  def __init__(self, key = None, value = None):
    self.__diccionario = set()
    if key != None:
      self.__diccionario.add(Diccionario.__TuplaDic(key,value))

  def __repr__(self):
    return str(self.__diccionario)

  ###Asignacion usando [], se recibe clave entre corchetes / Permite reemplazar aunque exista la clave
  def __setitem__(self, key = None, value = None):
    if key != None:
      if key in self:
        self.__diccionario.remove(key)
      self.__diccionario.add(Diccionario.__TuplaDic(key,value))

  ###No inserta si existe la clave, es decir, si la clave existe en el dicc no modifica el valor
  def insert(self, key = None, value = None):
    if key != None:
      self.__diccionario.add(Diccionario.__TuplaDic(key,value))

  ###Elimina si existe la clave, es decir, si la clave existe en el dicc elimina el par clave-valor
  ###Sino existe la clave, no hace nada
  def remove(self, key):
    if key in self:
        valor = self[key]
        self.__diccionario.remove(key)
        return valor

  ###Vacia dicc
  def clear(self):
    self.__diccionario = set()

  ###Clonar dicc
  def clone(self):
    return cp.deepcopy(self)

  ###Acceso a valores usando [], se recibe clave entre corchetes
  def __getitem__(self, key):
    value = None
    flag = False
    for tuplaDic in self.__diccionario:
      if tuplaDic == key:
        value = tuplaDic.getValue()
        flag = True
    if flag:
      return value
    else:
      raise Exception("No existe la clave %s en el diccionario" % (key))

  ###Retorna valor de la clave que se recibe por parametro
  def get(self, key):
    value = None
    flag = False
    for tuplaDic in self.__diccionario:
      if tuplaDic == key:
        value = tuplaDic.getValue()
        flag = True
    if flag:
      return value
    else:
      raise Exception("No existe la clave %s en el diccionario" % (key))

  ###Retorna lista con claves
  def keys(self):
    return [x.getKey() for x in self.__diccionario]

  ###Retorna lista con valores
  def values(self):
    return [x.getValue() for x in self.__diccionario]

  ###Operador "in"
  def __contains__(self, key):
    return key in self.__diccionario

  ###Tamaño de diccionario
  def len(self):
    return len(self.__diccionario)
  
# A partir del Ejercicio 2 vamos a trabajar fuera del TDA Diccionario usando la interface que creamos en el Ejercicio 1. Es decir,se pueden usar solo las operaciones de la interface, no se puede acceder a los componentes internos del TDA. Si necesitan estructuras auxiliares, pueden usar cualquiera de las estructuras que vimos hasta ahora: Arreglos, Listas, Pilas, Colas, Diccionarios.
# Ejercicio 2
# Escribir un programa que declare un Diccionario de <entero , entero> (clave entero y significado entero) y le agrege 4 pares. Luego debe mostrar el diccionario por pantalla y su tamaño.

# Finalmente, redefinir 2 significados y volver a imprimir.
def ejercicio2():
  diccionario = Diccionario()
  diccionario.insert(1,2)
  diccionario.insert(2,2)
  diccionario.insert(3,2)
  diccionario.insert(4,2)
  print(diccionario.len(), diccionario)

# Ejercicio 3
# Escribir un diccionario con sinónimos. Luego intentar insertar dos pares <clave , significado> con claves repetidas con la operacion insert y ver que sucede.

def ejercicio3():
    diccionario = Diccionario()
    diccionario.insert(1,2)
    diccionario.insert(2,2)
    diccionario.insert(3,3)
    diccionario.insert(4,3)
    diccionario.insert(3,3)
    diccionario.insert(4,10)
    print(diccionario.len(), diccionario)

# Ejercicio 4
# Escribir una función que dado una lista de enteros me devuelve otra(no necesariamente en el mismo orden) sin los numeros repetidos.

# Por ejemplo:

# Lista de entrada = [1 , 3 , 4 , 1 , 2 , 4 , 3 , 2]

# Lista de salida = [1 , 3 , 2, 4]

lista = [1 , 3 , 4 , 1 , 2 , 4 , 3 , 2]

def ejercicio4(lista: list):
    resultado = set()

    for elemento in lista:
        resultado.add(elemento)

    listaNueva = list()
    listaNueva = resultado.copy()

    return listaNueva
  
# Ejercicio 5
# Rehacer le ejercicio 4 pero retornando un diccionario en lugar de una lista.

# Por ejemplo:

# Lista de entrada = [1 , 3 , 4 , 1 , 2 , 4 , 3 , 2]

# Diccionario de salida = { (1 , None) , (3 , None) , (4 , None) , (2 , None) }

def ejercicio5(lista: list):
    d = Diccionario()

    for elemento in lista:
        d.insert(elemento, None)

    return d

# Ejercicio 6
# Escribir una función que recibe una lista de números como parámetro y devuelve un diccionario con los números de la lista como claves y la cantidad de apariciones de cada uno como su significado.

# Por ejemplo:

# Lista de entrada = [1 , 3 , 4 , 2 , 1 , 3 , 1 , 4 , 2 , 5 , 2]

# Diccionario de salida = { (1 , 3) , (3 , 2) , (4 , 2) , (2 , 3) , (5 , 1) }
lista2= [1 , 3 , 4 , 2 , 1 , 3 , 1 , 4 , 2 , 5 , 2]
  
def ejercicio6(lista):
    diccionario = Diccionario()

    for key in lista:
        if key in diccionario:
            diccionario.__setitem__(key, diccionario.get(key) +1)
        else:
            diccionario.insert(key,1)

    return diccionario
  
# Ejercicio 7
# Escribir una función que recibe dos diccionarios y devuelve otro con la mezcla de los dos, para las claves repetidas, se queda con los significados de primer diccionario.

# Por ejemplo:

# Diccionario de entrada 1 = { (1 , 3) , (3 , 2) , (4 , 4) , (2 , 3) , (5 , 1) }

# Diccionario de entrada 2 = { (10 , 3) , (3 , 5) , (2 , 30) , (8 , 1) , (9 , 3) }

# Diccionario de salida = { (1 , 3) , (3 , 2) , (4 , 4) , (2 , 3) , (5 , 1) , (10 , 3) , (8 , 1) , (9 , 3) }

dic1 = Diccionario()
dic1.insert(1 , 3)
dic1.insert(3,2)
dic1.insert(4,4)
dic1.insert(2,3) 
dic1.insert(5,1)

dic2 = Diccionario()
dic2.insert(10,3)
dic2.insert(3,5)
dic2.insert(2,30)
dic2.insert(8,1)
dic2.insert(9,3)

def ejercicio7(dic1: Diccionario,dic2: Diccionario):
    diccionario = Diccionario()
    diccionario = dic1.clone()
    for key in dic2.keys():
        if not key in diccionario:
            diccionario.insert(key, dic2[key])

    return diccionario

# Ejercicio 8
# Escribir una función que modele el problema de administrar las materias que cursa un alumno. Es decir que reciba un diccionario, un alumno y una materia y agregue esa materia a las materias que cursa.

# Nota: La lista de materias de cada alumno no debe tener materias repetidas.

# Por ejemplo:

# Diccionario = { ( "Alumno1" , ["Materia1" , "Materia2"] ) , ( "Alumno2", [ "Materia2" , "Materia3" , "Materia4" ] ) }

diccionario = Diccionario()
diccionario.insert('Kevin', set())

def ejercicio8(dic: Diccionario, alumnoNuevo:str, materia:str):

    for alumno in dic.keys():
        if alumno in dic:
            dic[alumno].add(materia)
        else:
           dic.insert(alumnoNuevo, {materia})

ejercicio8(diccionario,'Kevin','Estructura de datos')
ejercicio8(diccionario,'Kevin','Objetos 1')
print(diccionario)

# Ejercicio 9
# Tenemos un diccionario del tipo <Entero , Lista de enteros> (clave número entero, significado lista de enteros) que dado un numero X, guarda las posibles combinaciones de ese número con otros.

# Escribir una función que recibe un diccionario de este tipo y devuelve una lista con los posibles pares de números (en formato de tupla).

# Por ejemplo:

# Diccionario de entrada = { (5 , [5 , 3 , 7 ] ) , ( 8, [ 15 , 3 ] ) }

# Lista de salida = [ (5 , 5) ,(5 , 3) , (5 , 7) , (8 , 15) , (8 , 3) ]

# [ ]

# Ejercicio 10
# Escribir una función que haga lo inverso del Ejercicio 9.

# Por ejemplo:

# Lista de entrada = [ (5 , 5) ,(5 , 3) , (5 , 7) , (8 , 15) , (8 , 3) ]

# Diccionario de salida = { (5 , [5 , 3 , 7 ] ) , ( 8, [ 15 , 3 ] ) }

# [ ]

# Ejercicio 11
# Escribir el TDA MatrizDePixels, que modele una matriz de pixels (imagen) de N x M usando el tipo array del paquete numpy, donde cada pixel tiene un color representado por un número entero entre 0 y 255.

# Hacer las operaciones del TDA para crear una MatrizDePixels (por defecto llena de ceros), leer y escribir pixels.

# Luego pruebenla con estos ejemplos:

# a) Crear una MatrizDePixels de 100 x 100 y agregarle valores a dos pixels.

# b) Crear una MatrizDePixels de 100000 x 50000 y agregarle valores a dos pixels.

# Explicar porque el inciso b da un error

# [ ]

# Ahora escribir el TDA MatrizDePixelsDict, que modele una matriz de pixels (imagen) de N x M usando un diccionario de <(fila,columna) , pixel>, donde cada pixel tiene un color representado por un número entero entre 0 y 255 y el par (fila,columna) indica la posición del pixel en la matriz.

# Hacer las operaciones del TDA para crear una MatrizDePixelsDict (por defecto llena de ceros), leer y escribir pixels.

# Luego pruebenla con estos ejemplos:

# a) Crear una MatrizDePixelsDict de 100 x 100 y agregarle valores a dos pixels.

# b) Crear una MatrizDePixelsDict de 100000 x 50000 y agregarle valores a dos pixels.

# Explicar porque el inciso b ahora si funciona

# Nota: Si importan el paquete sys pueden usar la función sys.getsizeof(variable) que retorna el espacio que ocupa una variable en memoria.

# [ ]
# Ejercicio 12
# Implementar la suma matrices en el TDA MatrizDePixelsDict.