import Unidad5.tp7 as tp7
import Unidad6.tp8 as tp8
import Unidad7.tp10 as tp10

# Ejercicio 1
# Escribir una función que calcule la intersección de dos diccionarios de la siguiente forma:

# Si una clave está en ambos diccionarios, en la intersección el significado de dicha clave es una tupla con los valores de ambos diccionarios
# Si una clave está en uno solo de los diccionarios, no formará parte de la intersección.
# Ejemplo:
dic1 = tp7.Diccionario()
# {1:“casa” , 20:“perro” , 8:“gato” , 10:“mate” , 5:“auto”} 
dic1.insert(1,'casa')
dic1.insert(2,'gato')
dic1.insert(3, 10)
dic2 = tp7.Diccionario()
# {5:3 , 2:15 , 8:20 , 15:1 , 20:25}
dic2.insert(1,3)
dic2.insert(2,10)

# inter = interseccion(dic1, dic2) -> inter = {20 : (“perro”,25) , 8 : (“gato”,20) , 5 : (“auto”,3)}
def interseccionDiccionarios(diccionario1:tp7.Diccionario, diccionario2:tp7.Diccionario):
    interseccion = tp7.Diccionario()
    for clave in diccionario1.keys():
        if clave in diccionario2:
            interseccion.insert(clave,(diccionario1[clave],diccionario2[clave]))
    return interseccion

print(interseccionDiccionarios(dic1,dic2))
# Ejercicio 2
# Escribir una operación del TDA ABB, que calcule el promedio de los valores acumulados en el árbol. La operación puede calcular dos promedios distintos en función del valor de un parámetro de entrada: el primero es el promedio de los valores almacenados solo en las hojas del árbol, el segundo, el promedio teniendo en cuenta todos los elementos del árbol. Especificar la estructura de datos del tipo ABB y del NodoArbol utilizados.

class ABB:
  def promedio(self, tipo):
    promedio = None
    if not self.estaVacio():
      if tipo == "hojas":
        promedio = self.__raiz.sumaHojas() / self__raiz.cantHojas()
      else:
        promedio = self.__raiz.sumaTotal() / self.__raiz.peso()
    return promedio

  class __NodoArbol:
    def sumaTotal(self):
      total = self.dato
      if self.tieneIzquierdo():
        total += self.izquierdo.sumaTotal()
      if self.tieneDerecho():
        total += self.derecho.sumaTotal()
      return total
    def sumaHojas(self):
      hojas = 0
      if self.esHoja():
        hojas = self.dato
      else:
        if self.tieneIzquierdo():
          hojas += self.izquierdo.sumaHojas()
        if self.tieneDerecho():
          hojas += self.derecho.sumaHojas()
      return hojas
    def peso(self):
      pesoTotal = 1
      if self.tieneIzquierdo():
        pesoTotal += self.izquierdo.peso()
      if self.tieneDerecho():
        pesoTotal += self.derecho.peso()
      return pesoTotal
    def cantidadHojas(self):
      cantHojas = 0
      if self.esHoja():
        cantHojas = 1
      else:
        if self.tieneIzquierdo():
          cantHojas += self.izquierdo.cantidadHojas()
        if self.tieneDerecho():
          cantHojas += self.derecho.cantidadHojas()
      return cantHojas
    
# Ejercicio 3
# Escribir una operación del TDA Lista que inserte un dato de modo similar al insertar básico, al final de la lista (append). Pero ahora, no se debe permitir insertar datos repetidos, si un dato ya esta almacenado entonces la lista no varía. No se puede utilizar las operaciones insertar y buscar del TDA Lista. Especificar la estructura de datos del tipo Lista y del NodoLista utilizados.

def alFinalSinRepetir(self, dato):
  if self.estaVacia():
    self.__primero = Lista.__NodoLista(dato)
  else:
    nodoAux = self.__primero
    while nodoAux.tieneSiguiente() and nodoAux.dato != dato:
      nodoAux = nodoAux.siguiente
    if nodoAux.dato != dato:
      nodoAux.siguiente = Lista.__NodoLista(dato)

# Ejercicio 4
# Escribir la función maximoPorNumero que recibe una lista de pares (x,y) que indica que el número x está asociado al valor y.

# Se debe devolver un diccionario con clave x y significado (valor) y, donde y sea el máximo valor asociado a x.

# Se debe resolver usando las operaciones del TDA diccionario que vimos en clase,sin violar el encapsulamiento ni utilizando estructuras auxiliares.

# lista = [ (1,4) , (2,5) , (1,5) , (3,8) , (2,1) , (2,5) ]

# dic = maximoPorNumero(lista)

# Entonces, dic = {(1 , 5) , (2 , 5), (3, 8)}

def maximoPorNumero(listaTuplas):
  dicSalida = tp7.Diccionario()
  for tupla in listaTuplas:
    if tupla[0] not in dicSalida:
      dicSalida[tupla[0]] = tupla[1]
    else:
      if tupla[1] > dicSalida[tupla[0]]:
        dicSalida[tupla[0]] = tupla[1]
  return dicSalida

# print(maximoPorNumero([(1,4) , (2,5) , (1,20) , (3,8) , (2,1) , (2,5)]))
# {(1, 20), (2, 5), (3, 8)}

def maximoPorNumero(lista):
  dicSalida=Diccionario()
  for tupla in lista:
    if tupla[0] in dicSalida and tupla[1]>dicSalida.get(tupla[0]):
      dicSalida[tupla[0]]=tupla[1]
    else:
      dicSalida.insert(tupla[0],tupla[1])
  return dicSalida
# print(maximoPorNumero([(1,4) , (2,5) , (1,20) , (3,8) , (2,1) , (2,5)]))
# {(1, 20), (2, 5), (3, 8)}
# Ejercicio 5
# Escribir una operación del TDA Lista (enteros) que tome una lista y elimine todos los elementos impares, la operación NO debe retornar una nueva lista, sino modificar la lista con la cual se llama a la función. Definir la estructura de datos del tipo Lista y del NodoLista utilizados.

# Nota: No se puede utilizar la operación eliminar del TDA lista y el primer elemento siempre es par.

l = [2  , 4 , 2 ]

def esPar(num):
  return num%2==0

class Lista(Lista):
  def eliminarImpares(self):
    nodoAux=self.__primero
    while nodoAux.tieneSiguiente():
      if not esPar(nodoAux.siguiente.dato):
        nodoAux.siguiente=nodoAux.siguiente.siguiente
      else:
        nodoAux=nodoAux.siguiente

lista1 = Lista((2,1,1,2,1,2,1,2,1,1))

class Lista(Lista):
  def sacarImpares(self):
    if not self.estaVacia():
      self.__primero.sacarImpares()

  class __NodoLista(Lista.__NodoLista):
    def sacarImpares(self):
      if self.tieneSiguiente():
        if not esPar(self.siguiente.dato):
          self.siguiente = self.siguiente.siguiente
          self.sacarImpares()
        else:
          self.siguiente.sacarImpares()

lista1 = Lista((2,1,1,2,1,2,1,2,1,1))
print(lista1)
lista1.sacarImpares()
print(lista1)
# primero -> 2 -> 1 -> 1 -> 2 -> 1 -> 2 -> 1 -> 2 -> 1 -> 1 -|
# primero -> 2 -> 2 -> 2 -> 2 -|
# Ejercicio 6
# Escribir la operación sumaHastaNivel del TDA ABB que recibe un nivel N por parámetro y retorna la suma de todos los números en el ABB en nodos que estén a nivel menor o igual a N. La operación puede hacer uso de las operaciones del TDA ABB: estaVacio y del TDA NodoArbol: tieneIzquierdo y tieneDerecho

class ABB(ABB):
  def sumaHastaNivel(self, nivelN):
    suma = 0
    if not self.estaVacio():
      suma = self.__raiz.sumaHastaNivel(nivelN, 0)
    return suma

  class __NodoArbol(ABB.__NodoArbol):
    def sumaHastaNivel(self, nivelN, nivelActual):
      suma = 0

# Ejercicio 7
# Escribir la operación insertarEnPosI del TDA Lista que inserte una lista completa dentro de otra en una posición determinada. La función debe recibir como parámetro la lista que debe ser insertada y la posición de inserción. Si la posición es más grande que el tamaño de la lista original, la nueva lista se inserta al final. Definir la estructura de datos del TDA Lista utilizada. No se pueden utilizar las operaciones insertar y append del tipo Lista. No se puede usar el TDA lista de python.

# Ejemplo:

# Si lista1 = [3 , 5 , 8 , 2 , 6 , 7] y lista2 = [4 , 9 , 1 , 2]

# lista1.insertarEnPosI(lista2 , 3)

# Entonces: lista1 = [3 , 5 , 8 , 4 , 9 , 1 , 2 , 2 , 6 , 7]

class Lista(Lista):
  def insertarEnPosI(self, listaAInsertar, posIns):
    if not listaAInsertar.estaVacia():
      if posIns >= 0:
        if self.estaVacia():
          self.__primero = listaAInsertar.__primero
        else:
          nodoAux = listaAInsertar.__primero
          while nodoAux.tieneSiguiente():
            nodoAux = nodoAux.siguiente
          if posIns == 0:
            nodoAux.siguiente = self.__primero
            self.__primero = listaAInsertar.__primero
          else:
            nodoAux2 = self.__primero
            pos = 0
            while nodoAux2.tieneSiguiente() and pos < posIns-1:
              nodoAux2 = nodoAux2.siguiente
              pos += 1
            nodoAux.siguiente = nodoAux2.siguiente
            nodoAux2.siguiente = listaAInsertar.__primero

# lista1 = Lista((3 , 5 , 8 , 2 , 6 , 7))
# lista2 = Lista((4 , 9 , 1 , 2))
# print(lista1)
# print(lista2)
# lista1.insertarEnPosI(lista2,10)
# print()
# print(lista1)
# primero -> 3 -> 5 -> 8 -> 2 -> 6 -> 7 -|
# primero -> 4 -> 9 -> 1 -> 2 -|

# primero -> 3 -> 5 -> 8 -> 2 -> 6 -> 7 -> 4 -> 9 -> 1 -> 2 -|
# Ejercicio 8
# Escribir la función palabrasPorTamaño que recibe una lista de palabras (strings) y retorna un diccionario que posee como clave el tamaño de palabra y como significado una lista con las palabras de ese tamaño que forman parte de la lista de entrada.

# Se debe resolver usando las operaciones del TDA diccionario que vimos en clase, sin violar el encapsulamiento ni utilizando estructuras auxiliares.

# Por ejemplo:

# listaEntrada = [taza , perro , computadora , libro , en , casa , si]

# dic = palabrasPorTamaño(listaEntrada)

# Entonces, dic = { (4 , [taza , casa]) , (5 , [perro , libro]) , (11 , [computadora]) , (2 , [en , si]) }

def palabrasPorTamaño(listaPalabras):
  dicSalida = Diccionario()
  for palabra in listaPalabras:
    if len(palabra) in dicSalida:
      dicSalida[len(palabra)].append(palabra)
    else:
      dicSalida[len(palabra)] = [palabra]
  return dicSalida

# Ejercicio 9
# Escribir la operación sumaInternosMenores del TDA ABB que devuelva la suma de los elementos de los nodos internos del árbol que son menores a un valor N que se recibe por parámetro. Definir la estructura del TDA ABB utilizado. La función puede hacer uso de las siguientes operaciones del TDA ABB: estaVacio y del TDA NodoArbol: tieneIzquierdo, tieneDerecho y esHoja.
class Arbol:
    def sumaInternosMenores(self, N):
        if self.estaVacio():
            return 0
        else:
            return self.raiz.sumaInternosMenores(N)
        
    class Nodo:
        
        def sumaInternosMenores(self, N):
            suma = 0
            if self.esHoja():
                return 0

            if self.dato < N:
                suma += self.dato
            
            if self.tieneIzquierdo():
                suma += self.izquierdo.sumaInternosMenores(N)
            
            if self.tieneDerecho():
                suma += self.derecho.sumaInternosMenores(N)
            
            return suma

# Ejercicio 10
# Crear la operación insertarCeros del TDA Lista, que inserte un 0 (cero) entre 2 números pares consecutivos. La función no debe crear una nueva lista, debe modificar la lista con la cual se llama a la operación. Definir la estructura de datos del TDA Lista utilizada. No se pueden utilizar las operaciones insertar y append del tipo Lista.

# No se puede usar el TDA lista de python.

# Ejemplo:

# lista1 = [1 , 3 , 4 , 6 , 8 , 1 , 5 , 8 , 10 , 7]

# lista1.insertarCeros()

# Entonces, lista1 = [1 , 3 , 4 , 0 , 6 , 0 , 8 , 1 , 5 , 8 , 0 , 10 , 7]


    def insertarCeros(self):
        aux = self.primero

        while aux != None and aux.siguiente != None:
            if aux.valor % 2 == 0 and aux.siguiente.valor % 2 == 0:
                nuevo = self.Nodo(0)
                nuevo.siguiente = aux.siguiente
                aux.siguiente = nuevo
                self.tamaño += 1

            aux = aux.siguiente

# Ejercicio 11
# Escribir la función resta que recibe dos diccionarios como parámetro (dic1 y dic2) y retorna un nuevo diccionario con la resta los dos, con el siguiente criterio:

# Cuando una clave sólo está en el dic1, pasa al diccionario de salida con el significado original.

# Si una clave está en ambos diccionarios de entrada (dic1 y dic2), no pasa al diccionario de salida.

# Se debe resolver usando las operaciones del TDA diccionario que vimos en clase, sin violar el encapsulamiento ni utilizando estructuras auxiliares.

# Ejemplo:

# dic1 = {(1 , 4) , (3 , 6) , (8 , 14) , (4 , 12) , (2 , 6)} 
# dic2 = {(8 , 5) , (10 , 6) , (1 , 7) , (2 , 9) , (14 , 8)}

# dic3 = resta(dic1 , dic2)

# Entonces, dic3 = {(3 , 6) , (4 , 12)}

def restarDiccionarios(diccionario1:tp7.Diccionario, diccionario2: tp7.Diccionario):
    resta = tp7.Diccionario()
    for clave in diccionario1.keys():
        if not clave in diccionario2:
            resta.insert(clave,diccionario1[clave])
    return resta  
# Ejercicio 12
# Escribir la operación obtenerHermano del TDA ABB que recibe un número N y retorna el número del nodo hermano del nodo que contiene al número N. Dos nodos se definen como hermanos cuando tienen el mismo padre. Si el número N no está en el árbol o no tienen nodo hermano, la operación debe retornar None.

class ABB(ABB):
  def obtenerHermano(self, datoN):
    hermano = None
    if not self.estaVacio() and self.__raiz.dato != datoN:
      hermano = self.__raiz.obtenerHermano(datoN)
    return hermano

  class __NodoArbol(ABB.__NodoArbol):
    def obtenerHermano(self, datoN):
      hermano = None
      if datoN < self.dato:
        if self.tieneIzquierdo():
          if self.izquierdo.dato == datoN:
            if self.tieneDerecho():
              hermano = self.derecho.dato
          else:
            hermano = self.izquierdo.obtenerHermano(datoN)
      else:
        if self.tieneDerecho():
          if self.derecho.dato == datoN:
            if self.tieneIzquierdo():
              hermano = self.izquierdo.dato
          else:
            hermano = self.derecho.obtenerHermano(datoN)
      return hermano

arbol1 = ABB((50,40,30,20,45,35,28,60,70,55,65,68,80))
# print(arbol1.obtenerHermano(65))

# Escribir la función promedios que recibe una lista de materias (strings) y una lista de notas del mismo tamaño.
# Retorna un diccionario que posee como clave cada materia y como significado la nota promedio de cada
# materia.
# Se debe resolver usando las operaciones del TDA diccionario que vimos en clase, sin violar el encapsulamiento
# ni utilizando estructuras auxiliares.
materias = ["Intro Prog", "Objetos", "Estructura de Datos", "Intro Prog", "Inglés", "Objetos", "Estructura de Datos"]
notas = [4, 4, 4, 6, 7, 6, 6]

def promedios(listaMaterias, listaNotas):
  dicCantNotas = Diccionario()
  for elem in listaMaterias:
    if elem in dicCantNotas:
      dicCantNotas[elem] = dicCantNotas[elem] + 1
    else:
      dicCantNotas.insert(elem, 1)

  dicTotalNotas = Diccionario()
  for i in range(len(listaNotas)):
    if listaMaterias[i] in dicTotalNotas:
      dicTotalNotas[listaMaterias[i]] = dicTotalNotas[listaMaterias[i]] + listaNotas[i]
    else:
      dicTotalNotas.insert(listaMaterias[i], listaNotas[i])

  for el in dicTotalNotas.keys():
    dicTotalNotas[el] = dicTotalNotas[el] / dicCantNotas[el]
  return dicTotalNotas

# print(promedios(materias, notas))