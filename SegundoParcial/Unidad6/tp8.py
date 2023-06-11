# Ejercicio 1
# Implementar el TDA Lista enlazada simple, con las siguientes operaciones:

# __init__(): Constructor
# Vaciar
# Agregar elemento al final (append): Inserta nuevo nodo al final de la lista con el elemento que recibe como parámetro.
# Insertar elemento: Recibe un elemento y una posición como parámetro e inserta un nuevo nodo con el elemento en esa posición. Si la posicion es mayor al tamaño de la lista, el elemento se inserta al final.
# Obtener elemento (get): Recibe una posición y retorna el elemento del nodo en esa posición.
# Eliminar elemento (pop): Recibe una posición y elimina el nodo en esa posición.
# Obtener tamaño de lista.
# Esta vacía.
# Clonar
# __repr__(): Para poder imprimir una Lista por consola
# Nota: Cuando usamos posiciones en las listas, tener en cuenta que los indices empiezan en cero, es decir, el primer elemento de la lista esta en la posicion cero.

class Lista:
    class Nodo:
        def __init__(self,valor):
            self.valor = valor
            self.siguiente = None
            
        def __repr__(self):
            return ':' + self.valor.__repr__()

    def __init__(self):
        self.tamaño = 0
        self.primero= None

    def insertar(self, elemento):
        nuevo = self.Nodo(elemento)

        if self.tamaño == 0:
            self.primero = nuevo
        else: 
            aux = self.primero
            while aux.siguiente != None:
                aux = aux.siguiente

            aux.siguiente = nuevo
        self.tamaño += 1

    def __repr__(self):
      resultado = str(self.tamaño) 
      if (self.tamaño > 0):
        aux = self.primero
        resultado = resultado + aux.__repr__()
        while (aux.siguiente != None):  
          aux = aux.siguiente  
          resultado = resultado + aux.__repr__() 
      return resultado  
    
    def obtener(self, posicion = 0):
        aux = self.primero
        contador = 0
        
        if self.tamaño >= posicion:
            while contador < posicion:
                aux = aux.siguiente
                contador +=1 
        else:
            raise Exception('Posicion fuera de rango')

        return aux.valor
    
    def eliminar(self, posicion):
        if self.tamaño >= posicion and posicion >= 0:

            if self.tamaño == 1:
                self.primero = None
            else:

                if posicion == 0:
                    self.primero = self.primero.siguiente
                    
                else:
                    aux = self.primero
                    contador = 0

                    while contador < posicion -1:
                        aux = aux.siguiente
                        contador +=1 

                    aux.siguiente = aux.siguiente.siguiente

            self.tamaño -= 1
        else:
            raise Exception('Posicion inválida')
        
    def tamaño(self):
        cantidad = 0
        aux = self.primero
        while aux != None:
            cantidad += 1
            aux = aux.siguiente
        return cantidad
    
    def estaVacia(self):
        return self.primero == None
    
    def insertarEnPosicion(self, elemento, posicion):

        if self.tamaño >= posicion and posicion >= 0:

            if self.tamaño == 0 or posicion == self.tamaño:
                self.insertar(elemento)
                
            else:
                nuevo = self.Nodo(elemento)

                if posicion == 0:
                    nuevo.siguiente = self.primero
                    self.primero = nuevo
                    
                else:
                    aux = self.primero
                    contador = 0

                    while contador < posicion -1 :
                        aux = aux.siguiente
                        contador +=1 

                    nuevo.siguiente = aux.siguiente
                    aux.siguiente = nuevo

                self.tamaño += 1
        else:
            raise Exception('Posicion inválida')

    def eliminarElemento(self, elemento):
        contador = 0
        listaDePosiciones = self.buscarElemento(elemento)

        while not listaDePosiciones.estaVacia():
            posicionAEliminar = listaDePosiciones.obtener()
            self.eliminar(posicionAEliminar)
            contador += 1
            listaDePosiciones = self.buscarElemento(elemento)

        return contador
                
    def buscarElemento(self, elemento):
        listaDePosiciones = Lista()

        for i in range(self.tamaño):
            if self.obtener(i) == elemento:
                listaDePosiciones.insertar(i)

        return listaDePosiciones
    
    def ponerInicioAlFinal(self):
        self.insertar(self.obtener(0))
        self.eliminar(0)

    def ponerFinalAlInicio(self):
        self.insertarEnPosicion(self.obtener(self.tamaño-1),0)
        self.eliminar(self.tamaño-1)

    def reemplazarElemento(self, elementoNuevo, elementoAReemplazar):
        listaDePosiciones = self.buscarElemento(elementoAReemplazar)
        self.eliminarElemento(10)

        for i in range(listaDePosiciones.tamaño):
            self.insertarEnPosicion(elementoNuevo,listaDePosiciones.obtener(i))
            
    def duplicar(self):

        for i in range(self.tamaño):
            self.insertar(self.obtener(i))
        
    def recorridoSalteado(self):
        listaSalteada = Lista()
        for i in range(self.tamaño):
            if i%2 == 0:
                listaSalteada.insertar(self.obtener(i))
            
        print(listaSalteada)

    def recorridoParImpar(self):
        aux = self.primero
        contador = 0

        while aux.siguiente != None:
            if contador < self.tamaño:
                if self.obtener(contador)%2 == 0:
                    print(self.obtener(contador))
                    contador+=1
                else:
                    print(self.obtener(contador))
                    contador +=2

    def reemplazarElementoMultiplicado(self, comparador, multiplicador):

        for i in range(self.tamaño):
            if self.obtener(i) >= comparador:
                nuevoElemento = self.obtener(i)*multiplicador
                self.reemplazar(nuevoElemento,i)
        
    def reemplazar(self, elemento, posicion):
            self.eliminar(posicion)
            self.insertarEnPosicion(elemento,posicion)
            

# Ejercicio 2
# Escribir una operación del TDA Lista que intercambie los dos primeros nodos de la lista.
lista = Lista()
lista.insertar(10)
lista.insertar(66)
lista.insertar(99)
lista.insertar(10)
lista.insertar(10)
lista.insertar(88)

lista.reemplazarElementoMultiplicado(50,0)
print(lista)

def ejercicio2(lista):

    var = lista.obtener(0)
    var2 = lista.obtener(1)

    lista.eliminar(0)
    lista.insertarEnPosicion(var2,0)
    lista.eliminar(1)
    lista.insertarEnPosicion(var,1)

    print(lista)

# Ejercicio 3
# Escribir la operación del TDA Lista buscaElemento() que busque un elemento que recibe por parámetro. La operación debe retornar una lista con las ubicaciones del elemento en la lista de entrada.

# Por ejemplo:insertarEnPosicion

# lista1 = [ 2 , 2 , 1 , 4 , 2 , 8 , 9 , 2 , 10]

# posiciones = lista1.buscaElemento(2)

# Entonces, posiciones = [ 0 , 1 , 4 , 7 ]

# Ejercicio 4
# Escribir una operación del TDA Lista que elimine todas las ocurrencias de un elemento que recibe por parámetro y devuelva la cantidad de veces que se elimino el elemento. Se deben eliminar todos los nodos que contengan al elemento.

# Por ejemplo:

# lista1 = [ 2 , 2 , 1 , 4 , 2 , 2 , 8 , 9 , 2 , 10]

# cant = lista1.eliminarOcurrencias(2)

# Entonces, cant = 5 y lista1 = [ 1 , 4 , 8 , 9 , 10 ]


# Ejercicio 5
# Escribir una operación del TDA Lista que saque el nodo que esta al inicio de la lista (posición cero) y lo ponga en el final. Hacer otra que haga lo contrario, saque el nodo del final y lo ponga al inicio.
# [ ]

# Ejercicio 6
# Escribir una operación del TDA Lista que reemplace todas las ocurrencias de un numero por otro. Ambos números los recibe por parámetro.

# Por ejemplo:

# lista1 = [ 2 , 1 , 4 , 8 , 9 , 2 , 5 , 12 , 10]

# lista1.reemplazar(2,3) #Reemplaza todos los 2 por 3

# Entonces, lista1 = [ 3 , 1 , 4 , 8 , 9 , 3 , 5 , 12 , 10 ]

# [ ]

# Ejercicio 7
# Escribir la operación duplicar() del TDA Lista que duplica el contenido de una lista.

# Por ejemplo:

# lista1 = [ 2 , 1 , 4 , 8 , 9 ]

# lista1.duplicar()

# Entonces, lista1 = [ 2 , 1 , 4 , 8 , 9 , 2 , 1 , 4 , 8 , 9 ]

# [ ]

# Ejercicio 8
# Los recorridos de listas normalmente pasan por todos los nodos, empezando por el primero, luego al siguiente, etc, como en la siguiente figura:

# texto alternativo

# Escribir una operación del TDA Lista que recorra la lista salteandose de a un nodo y mostrando por pantalla los elementos de los nodos visitados. El recorrido debe ser asi:

# texto alternativo

# Por ejemplo:

# lista1 = [ 2 , 1 , 4 , 8 , 9 , 12 , 5 , 8 ]

# lista1.recorridoSalteado()

# 2

# 4

# 9

# 5

# Nota: No es correcto hacer un recorrido secuencial e ir contando las posiciones, lo correcto es solo visitar los nodos que nos interesan

# [ ]

# Ejercicio 9
# Vamos con otro tipo de recorrido de listas, escribir una operación del TDA Lista que recorra la lista de la siguiente manera (mientras va imprimiendo los elementos del nodo visitado):

# Si el elemento del nodo visitado es par, seguimos por el siguiente
# Si el elemento del nodo visitado es impar, nos salteamos el siguiente y seguimos con el otro
# El recorrido debe ser asi:

# texto alternativo

# Por ejemplo:

# lista1 = [ 2 , 5 , 1 , 9 , 8 , 10 , 7 ]

# lista1.recorridoParImpar()

# 2

# 5

# 9

# 10

# 7

# [ ]

# Ejercicio 10
# Escribir una operación del TDA Lista que recibe dos números por parámetro. La operación recorre la lista, si el elemento del nodo es menor que el primer parámetro se deja igual, si es mayor o igual, se reemplaza por el mismo número multiplicado por el otro parámetro.

# Por ejemplo:

# lista1 = [ 2 , 1 , 4 , 8 , 9 , 12 , 0 , 10 , 1 , 4 ]

# lista1.reemplazaMayores(6,3) #Multiplica por 3 los mayores o iguales a 6, el resto queda igual

# Entonces, lista1 = [ 2 , 1 , 4 , 24 , 27 , 36 , 0 , 30 , 1 , 4 ]

# [ ]

# Ejercicio 11
# Escribir una operación del TDA Lista que recibe dos números por parámetro: una posición y un número nuevo. Recorre la lista hasta la posición y reemplaza el número de la lista por el nuevo.

# Por ejemplo:

# lista1 = [ 2 , 1 , 4 , 8 , 9 , 12 , 0 , 10 , 1 , 4 ]

# lista1.reemplazar(2,20) #Reemplaza el número en la posición 2 por 20

# Entonces, lista1 = [ 2 , 1 , 20 , 8 , 9 , 12 , 0 , 10 , 1 , 4 ]

# [ ]

# Ejercicio 12
# Escribir la operación insertarOrdenado() del TDA Lista, que se llama desde una lista ordenada e inserta un número que recibe por parámetro en el lugar correcto (manteniendo el orden).

# Por ejemplo:

# lista1 = [ 2 , 5 , 9 , 12 , 25 , 32 ]

# lista1.insertarOrdenado(10)

# Entonces, lista1 = [ 2 , 5 , 9 , 10 , 12 , 25 , 32 ]

# [ ]
