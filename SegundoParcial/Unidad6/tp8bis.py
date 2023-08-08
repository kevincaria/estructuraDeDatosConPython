class Lista:
    class Nodo:
        def __init__(self,valor):
            self.valor = valor
            self.siguiente = None

        def __repr__(self):
            return ':' + self.valor.__repr__()
        
    def __init__(self):
        self.tamaño = 0
        self.primero = None

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

    def obtener(self, posicion):
        if self.tamaño == 0:
            return self.__repr__()
        elif self.tamaño >= posicion:
            aux = self.primero
            contador = 0
            while posicion > contador:
                aux = aux.siguiente
                contador += 1
            resultado = aux.valor
        else:
            raise Exception(' Posicion invalida')
        return resultado

    def __repr__(self):
        resultado = str(self.tamaño)
        if (self.tamaño > 0):
            aux = self.primero
            resultado = resultado + aux.__repr__()
            while aux.siguiente != None:
                aux = aux.siguiente
                resultado = resultado + aux.__repr__()
        return resultado
    
    def vaciar(self):
        self.primero = None
        self.tamaño = 0

    def estaVacia(self):
        return self.tamaño == 0
    
    def insertarPosicion(self, posicion, dato):
        nuevo = self.Nodo(dato)
        if self.estaVacia():
            self.primero = nuevo
        elif posicion == 0:
            nuevo.siguiente = self.primero
            self.primero = nuevo
        elif posicion <= self.tamaño:
            aux = self.primero
            contador = 0
            while posicion-1 > contador:
                aux = aux.siguiente
                contador += 1
            nuevo.siguiente = aux.siguiente
            aux.siguiente = nuevo
        else:
            raise Exception('Posicion invalida')
        self.tamaño += 1
        
    def eliminar(self, posicion):
        if self.estaVacia():
            raise Exception('La lista esta vacia')
        elif posicion == 0 and self.tamaño > 1:
            self.primero = self.primero.siguiente
        elif self.tamaño >= posicion:
            aux = self.primero
            contador = 0
            while  contador < posicion -1:
                aux = aux.siguiente
                contador += 1
            aux.siguiente = aux.siguiente.siguiente
        self.tamaño -= 1

# Ejercicio 3
# Escribir la operación del TDA Lista buscaElemento() que busque un elemento que recibe por parámetro. La operación debe retornar una lista con las ubicaciones del elemento en la lista de entrada.
    def buscarElemento(self,elemento):
        listaResultado = Lista()
        if self.estaVacia():
            raise Exception('La lista esta vacia')
        else:
            aux = self.primero
            contador = 0
            while aux.siguiente != None:
                if aux.valor == elemento:
                    listaResultado.insertar(contador)
                aux = aux.siguiente
                contador += 1
            if aux.valor == elemento:
                    listaResultado.insertar(contador)
        return listaResultado

# Ejercicio 4
# Escribir una operación del TDA Lista que elimine todas las ocurrencias de un elemento que recibe por parámetro y devuelva la cantidad de veces que se elimino el elemento. Se deben eliminar todos los nodos que contengan al elemento.
    def eliminarOcurrencias(self, elemento):
        listaOcurrencias = self.buscarElemento(elemento)
        contador = 0
        while not listaOcurrencias.estaVacia():
            self.eliminar(listaOcurrencias.obtener(0))
            contador += 1
            listaOcurrencias = self.buscarElemento(elemento)
        return contador
    
# Ejercicio 5
# Escribir una operación del TDA Lista que saque el nodo que esta al inicio de la lista (posición cero) y lo ponga en el final. Hacer otra que haga lo contrario, saque el nodo del final y lo ponga al inicio.
    def ponerInicioAlFinal(self):
        if self.estaVacia():
            raise Exception('La lista esta vacia')
        else:
            inicio = self.primero
            self.eliminar(0)
            self.insertar(inicio)

    def ponerFinalAlInicio(self):
        if self.estaVacia():
            raise Exception('La lista esta vacia')
        else:
            posicionFinal = self.tamaño-1
            final = self.obtener(posicionFinal)
            self.eliminar(posicionFinal)
            self.insertarPosicion(0,final)

# Ejercicio 6
# Escribir una operación del TDA Lista que reemplace todas las ocurrencias de un numero por otro. Ambos números los recibe por parámetro.

    def reemplazar(self, viejo, nuevo):
        lista = self.buscarElemento(viejo)
        self.eliminarOcurrencias(viejo)
        
        for i in range(lista.tamaño):
            self.insertarPosicion(lista.obtener(i), nuevo)
# Ejercicio 7
# Escribir la operación duplicar() del TDA Lista que duplica el contenido de una lista.

    def duplicar(self):
        recorrido = self.tamaño
        for i in range(recorrido):
            self.insertar(self.obtener(i))

# Ejercicio 8
# Los recorridos de listas normalmente pasan por todos los nodos, empezando por el primero, luego al siguiente, etc, como en la siguiente figura:

# texto alternativo

# Escribir una operación del TDA Lista que recorra la lista salteandose de a un nodo y mostrando por pantalla los elementos de los nodos visitados. El recorrido debe ser asi:

# texto alternativo

    def recorridoSalteado(self):
        if self.estaVacia():
            raise Exception('La lista esta vacia')
        else:
            aux = self.primero
            while aux.siguiente != None:
                print(aux.valor)
                aux = aux.siguiente.siguiente
            print(aux.valor)
                
# Ejercicio 9
# Vamos con otro tipo de recorrido de listas, escribir una operación del TDA Lista que recorra la lista de la siguiente manera (mientras va imprimiendo los elementos del nodo visitado):

# Si el elemento del nodo visitado es par, seguimos por el siguiente
# Si el elemento del nodo visitado es impar, nos salteamos el siguiente y seguimos con el otro

    def recorridoParImpar(self):
        if self.estaVacia():
            raise Exception('La lista esta vacia')
        else:
            aux = self.primero
            while aux.siguiente != None:
                print(aux.valor)
                if aux.valor %2 == 0:
                    aux = aux.siguiente
                else:
                    aux = aux.siguiente.siguiente
            print(aux.valor)
# Ejercicio 10
# Escribir una operación del TDA Lista que recibe dos números por parámetro. La operación recorre la lista, si el elemento del nodo es menor que el primer parámetro se deja igual, si es mayor o igual, se reemplaza por el mismo número multiplicado por el otro parámetro.

    def reemplazaMayores(self, multiplicador, mayor):
        if self.estaVacia():
            raise Exception('La lista esta vacia')
        else:
            aux = self.primero
            contador = 0
            while aux != None:
                if aux.valor >= mayor:
                    nuevoValor = multiplicador*aux.valor
                    self.eliminar(contador)
                    self.insertarPosicion(contador,nuevoValor)
                aux = aux.siguiente
                contador += 1

# Ejercicio 11
# Escribir una operación del TDA Lista que recibe dos números por parámetro: una posición y un número nuevo. Recorre la lista hasta la posición y reemplaza el número de la lista por el nuevo.

    def reemplazar(self, posicion, valor):
        nuevo = self.Nodo(valor)
        if self.estaVacia():
            raise Exception('La lista esta vacia')
        else:
            if posicion -1 <= self.tamaño:
                if posicion == 0:
                    nodoSiguiente = self.primero.siguiente
                    self.primero = nuevo
                    self.primero.siguiente = nodoSiguiente
                else:
                    aux = self.primero
                    contador = 0
                    while contador < posicion -1:
                        aux = aux.siguiente
                        contador += 1
                    nodoSiguiente = aux.siguiente
                    aux.siguiente = nuevo
                    nuevo.siguiente = nodoSiguiente
            else:
                raise Exception('Posicion fuera de rango')
# Ejercicio 12
# Escribir la operación insertarOrdenado() del TDA Lista, que se llama desde una lista ordenada e inserta un número que recibe por parámetro en el lugar correcto (manteniendo el orden).


    def insertarOrdenado(self, dato):
        if self.estaVacia():
            nuevo = self.Nodo(dato)
            self.primero = nuevo
        else:
            if self.primero.valor >= dato:
                self.insertarPosicion(0,dato)
            else:
                aux = self.primero
                posicion = 0
                insertado = False
                while  aux.valor < dato and aux.siguiente != None:
                    posicion += 1
                    if aux.siguiente.valor >= dato:
                        self.insertarPosicion(posicion, dato)
                        insertado = True
                    aux = aux.siguiente
                if aux.valor < dato and not insertado:
                    self.insertar(dato)

    def eliminarDesdeHasta(self,inicio,fin):
        contador = 0
        if self.estaVacia():
            raise Exception('La lista esta vacia')
        elif self.tamaño == 1:
            self.primero = None
        elif inicio == 0:
            aux = self.primero
            while aux.siguiente != None and contador < fin:
                aux = aux.siguiente
                contador +=1

            self.primero = aux.siguiente
        else:
            auxInicio = self.primero
            auxFin = self.primero
            while auxFin.siguiente != None and contador < fin:
                if contador < inicio -1:
                    auxInicio = auxInicio.siguiente
                auxFin = auxFin.siguiente
                contador += 1
            auxInicio.siguiente = auxFin.siguiente

# Ejercicio 3
# Escribir una operación del TDA Lista que inserte un dato de modo similar al insertar básico, al final de la lista (append). Pero ahora, no se debe permitir insertar datos repetidos, si un dato ya esta almacenado entonces la lista no varía. No se puede utilizar las operaciones insertar y buscar del TDA Lista. Especificar la estructura de datos del tipo Lista y del NodoLista utilizados.

    def insertarSinRepetido(self, dato):
        nuevo = self.Nodo(dato)
        if self.estaVacia():
            self.primero = nuevo
        else:
            aux = self.primero
            repetido = False
            while aux.siguiente != None:
                if aux.valor == dato:
                    repetido = True
                aux = aux.siguiente
            if not repetido and aux.valor != dato:
                aux.siguiente = nuevo

# # Ejercicio 5
# # Escribir una operación del TDA Lista (enteros) que tome una lista y elimine todos los elementos impares, la operación NO debe retornar una nueva lista, sino modificar la lista con la cual se llama a la función. Definir la estructura de datos del tipo Lista y del NodoLista utilizados.

    def eliminarImpares(self):
        if self.estaVacia():
            raise Exception('La lista esta vacia')
        else:       
            puntero = self.primero
            aux = self.primero
            while aux.siguiente != None:
                if puntero.siguiente.valor %2 != 0 :
                    aux.siguiente = aux.siguiente.siguiente
                aux = aux.siguiente
                puntero = puntero.siguiente

# # Ejercicio 7
# # Escribir la operación insertarEnPosI del TDA Lista que inserte una lista completa dentro de otra en una posición determinada. La función debe recibir como parámetro la lista que debe ser insertada y la posición de inserción. Si la posición es más grande que el tamaño de la lista original, la nueva lista se inserta al final. Definir la estructura de datos del TDA Lista utilizada. No se pueden utilizar las operaciones insertar y append del tipo Lista. No se puede usar el TDA lista de python.
    def insertarListaEnPosicion(self,lista,posicion):
        contador = 0
        if self.estaVacia():
            self.primero = lista.primero
        elif posicion == 0: 
            primeroNodo = self.primero
            self.primero = lista.primero
            aux = self.primero
            
            while contador != lista.tamaño-1:
                aux = aux.siguiente
                contador += 1
            aux.siguiente = primeroNodo
        elif posicion <= self.tamaño -1:
            auxInicio = self.primero
            auxFin = self.primero
            auxLista = lista.primero
            while contador < posicion - 1:
                auxInicio = auxInicio.siguiente
                auxFin = auxFin.siguiente
                contador += 1
            auxFin = auxFin.siguiente

            while auxLista.siguiente != None:
                auxLista = auxLista.siguiente

            auxInicio.siguiente = lista.primero
            auxLista.siguiente = auxFin

        else:
            raise Exception('Posicion Invalida')

# # Ejercicio 10
# # Crear la operación insertarCeros del TDA Lista, que inserte un 0 (cero) entre 2 números pares consecutivos. La función no debe crear una nueva lista, debe modificar la lista con la cual se llama a la operación. Definir la estructura de datos del TDA Lista utilizada. No se pueden utilizar las operaciones insertar y append del tipo Lista.

    def insertarCeros(self):
        
        if self.estaVacia():
            raise Exception('La lista está vacía')
        else:
            aux = self.primero
            while aux.siguiente.siguiente != None:
                if aux.valor % 2 == 0 and aux.siguiente.valor %2 == 0:
                    nuevo = self.Nodo(0)
                    nuevo.siguiente = aux.siguiente
                    aux.siguiente = nuevo
                
                aux = aux.siguiente