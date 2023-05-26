import numpy as np
import copy as cp
# Ejercicio 1
# Implementar el TDA Pila (Stack), con las siguientes operaciones:

# Crear (init())
# Vaciar
# Apilar elemento (push)
# Desapilar elemento (pop)
# Obtener primer elemento (top)
# Obtener tamaño de pila
# Clonar
# Esta vacía.
# repr(). Para poder imprimir una Pila por consola
class Pila:
   def __init__(self, lista:list = []):
      self.estructura: list = lista

   def __repr__(self):
      return self.estructura.__repr__()
    
   def vaciar(self):
      self.estructura.clear()

   def apilarElemento(self, elemento):
      self.estructura.append(elemento)

   def desapilarElemento(self):
      if not self.estaVacia():
        return self.estructura.pop()
      else:
         raise Exception('No hay elementos para desapilar')
  
   def primerElemento(self):
      return self.estructura[self.tamaño()-1]
    
   def tamaño(self):
      return len(self.estructura)
    
   def clonar(self):
       return Pila(self.estructura.copy())

   def estaVacia(self):
      return self.tamaño() == 0
   
   def apilarPila(self,pilaAApilar):
      while not(pilaAApilar.estaVacia()):
         self.apilarElemento(pilaAApilar.desapilarElemento())

   def apilarPilaOrdenada(self, pilaAApilar):
      pilaAux = Pila()
      while not(pilaAApilar.estaVacia()):
         pilaAux.apilarElemento(pilaAApilar.desapilarElemento())
      self.apilarPila(pilaAux)

pilaEnteros = Pila([1,2,3])
pilaOtrosEnteros = Pila([1, 1, 1])
    
# A partir del Ejercicio 2 vamos a trabajar fuera del TDA Pila usando la interface que 
# creamos en el Ejercicio 1. Es decir, se pueden usar solo las operaciones de la interface, 
# no se puede acceder a los componentes internos del TDA. Si necesitan estructuras auxiliares, 
# pueden usar otra pila, arreglos o listas.
# Ejercicio 2
# Escribir un programa que declare una pila de enteros y le apile 4 elementos. 
# Luego debe mostrar la pila y su tamaño, desapilar 2 elementos y volver a imprimirla junto 
# con el nuevo tamaño.

def ejercicio2():
  pilaEnteros = Pila([1,2,3,4,5,6])
  print(pilaEnteros)
  pilaEnteros.apilarElemento(7)
  pilaEnteros.apilarElemento(7)
  pilaEnteros.apilarElemento(7)
  pilaEnteros.apilarElemento(7)
  print(pilaEnteros)
  print(pilaEnteros.tamaño())
  pilaEnteros.desapilarElemento()
  pilaEnteros.desapilarElemento()
  print(pilaEnteros)

# Ejercicio 3
# Escribir una función que invierta el orden de una pila. No debe devolver una nueva 
# pila invertida, sino invertir la pila que ingresa por parámetro.

def invertirPila(pila: Pila):
   pilaAux = pila.clonar()
   pila.vaciar()
   pila.apilarPila(pilaAux)

# Ejercicio 4
# Escribir una función que toma el último elemento de una pila(la base) y lo ponga 
# en la cima (de la misma pila), respetando el orden del resto de los elementos. 
# Utilizar una pila auxiliar.

def Ejercicio4(pila:Pila):
   pilaAux = Pila()
   pilaAux.apilarPila(pila)
   base = pilaAux.desapilarElemento()
   pila.vaciar()
   pila.apilarPila(pilaAux)
   pila.apilarElemento(base)

# Ejercicio 5
# Escribir una función que coloque en el fondo de una pila un nuevo elemento.
def ejercicio5(pila:Pila, elemento):
   pilaAux = pila.clonar()
   pila.vaciar()
   pila.apilarElemento(elemento)
   pila.apilarPilaOrdenada(pilaAux)
   return pila
 
# Ejercicio 6
# Escribir una función que elimine de una pila todas las ocurrencias de un elemento dado. Usar una pila auxiliar.

def ejercicio6(pila:Pila, elemento):
   pilaAux = Pila()

   while not pila.estaVacia():
      elementoAMirar = pila.desapilarElemento()
      if not elementoAMirar == elemento:
         pilaAux.apilarElemento(elementoAMirar)

   pila.apilarPilaOrdenada(pilaAux)
   return pila

# Ejercicio 7
# Escribir un función que duplique el contenido de una pila.

# Por ejemplo, si la pila de entrada es:

# Pila = 8, 5, 6, 9

# Luego de la función la salida debe ser:

# pilaSalida = 8, 5, 6, 9, 8, 5, 6, 9
def ejercicio7(pila:Pila):
   pilaAux = pila.clonar()
   pila.apilarPilaOrdenada(pilaAux)

# Ejercicio 8
# Escribir una función que realiza el cálculo de la suma de dos números enteros de 
# muchos dígitos (los dos números tienen la misma cantidad de dígitos). 
# La función recibe dos pilas por parámetro, 
# las que almacenan los dígitos de los números a sumar 
# (esta pilas no deben estar modificadas al terminar la función). 
# La función debe retornar una nueva pila con el resultado.

# Por ejemplo para sumar: 85699625 + 75426652

# Las pilas de entrada a la función son:

# Pila1 = 8, 5, 6, 9, 9, 6, 2, 5

# Pila2 = 7, 5, 4, 2, 6, 6, 5, 2

# La salida:

# pilaSalida = 1, 6, 1, 1, 2, 6, 2, 7, 7

def ejercicio8(pila1:Pila,pila2:Pila):
   primerEntero = 0
   segundoEntero = 0
   multiplicador = 1

   while not (pila1.estaVacia() and pila2.estaVacia()):
      primerEntero = pila1.desapilarElemento() * multiplicador
      segundoEntero = pila2.desapilarElemento() * multiplicador
      multiplicador = multiplicador*10

   return primerEntero + segundoEntero

# Ejercicio 9
# Escribir la función “reemplazar”, que recibe como parámetro una pila de enteros y 
# dos números enteros: “viejo” y “nuevo”. 
# La función debe modificar la pila ingresada por parámetro, 
# reemplazando cada ocurrencia del número “viejo” por el “nuevo”.

def ejercicio9(pila:Pila, viejo, nuevo):
   pilaAux = Pila()

   while not pila.estaVacia():
      elementoAMirar = pila.desapilarElemento()
      if elementoAMirar == viejo:
         pilaAux.apilarElemento(nuevo)
      else:
         pilaAux.apilarElemento(elementoAMirar)

   pila.apilarPilaOrdenada(pilaAux)
   return pila

# Ejercicio 10
# Escribir una función que recibe una pila de enteros y retorna dos pilas, 
# una con solo los números pares y otra con solo los impares, 
# provenientes de la pila de entrada. Al finalizar la función, 
# la pila de entrada no debe estar modificada.

def ejercicio10(pila:Pila):
   pilaAux = pila.clonar()
   pilaPares = Pila()
   pilaImpares = Pila()

   while not pilaAux.estaVacia():
      elementoAMirar = pilaAux.desapilarElemento()
      if elementoAMirar%2 == 0:
         pilaPares.apilarElemento(elementoAMirar)
      elif elementoAMirar%2 != 0:
         pilaImpares.apilarElemento(elementoAMirar)
         
   return pilaPares,pilaImpares

# Parte 2: Colas dinámicas
# Ejercicio 11
# Implementar el TDA Cola (Queue), con las siguientes operaciones:

# Crear (init())
# Vaciar
# Encolar elemento (enqueue)
# Desancolar elemento (dequeue)
# Obtener primer elemento (top)
# Obtener tamaño de cola
# Clonar
# Esta vacía.
# repr(). Para poder imprimir una Cola por consola
 

# A partir del Ejercicio 12 vamos a trabajar fuera del TDA Cola usando la interface que 
# creamos en el Ejercicio 11. Es decir, se pueden usar solo las operaciones de la interface, 
# no se puede acceder a los componentes internos del TDA. 
# Si necesitan estructuras auxiliares, pueden usar otra cola, pilas, arreglos o listas.
# Ejercicio 12
# Escribir una función que invierta el orden de una cola. 
# No debe devolver una nueva cola invertida, sino invertir la cola que ingresa por parámetro.

 

# Ejercicio 13
# Escribir una función que extraiga el primer elemento de una cola y lo ponga en el final, 
# respetando el orden del resto de los elementos.

 

# Ejercicio 14
# Escribir una función que coloque en el principio de una cola un nuevo elemento.

 

# Ejercicio 15
# Escribir una función que elimine de una cola todas las ocurrencias de un elemento dado.

 

# Ejercicio 16
# Escribir una función que recibe una cola de enteros y genera dos colas: 
# una con los números primos y otra con los números no primos, de la cola de entrada. 
# Al terminar la función, la cola de entrada no debe estar modificada.

 

# Ejercicio 17
# Implementar la función "mezcla" de dos colas, 
# que recibe como parámetros dos colas ordenadas de menor a mayor y 
# devuelve una nueva cola con la unión de ambas colas de entrada con 
# sus elementos ordenados de la misma manera.

 
# Ejercicio 18
# Implementar la función que recibe como parámetro una cola y
#  elimina todos los números pares.