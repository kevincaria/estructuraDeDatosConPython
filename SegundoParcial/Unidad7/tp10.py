# Ejercicio 1
# Implementar el TDA Árbol binario de búsqueda, con las siguientes operaciones:

# En el Tipo NodoArbol:

# __init__(): Constructor.
# Tiene hijo izquierdo.
# Tiene hijo derecho.
# Obtener grado.
# Es hoja.
# Predecesor de un nodo: Retorna el nodo predecesor.
# Sucesor de un nodo: Retorna el nodo sucesor.
# En el Tipo ABB:

# __init__(): Constructor.
# Vaciar.
# Esta vacio.
# Mostrar elementos en PreOrden.
# Mostrar elementos en InOrden: Prueben que pasa si en lugar de ir primero al subarbol izquierdo y luego al subarbol derecho, van primero al derecho y luego al izquierdo.
# Mostrar elementos en PostOrden.
# Insertar elemento: Inserta nuevo nodo en el lugar que corresponde en el árbol con el elemento que recibe como parámetro.
# Buscar elemento: Recibe un elemento y retorna True si el elemento esta en el árbol y False en caso contrario.
# Eliminar elemento: Recibe un elemento y elimina el nodo que lo contiene.
# Clonar.
# Obtener peso del arbol.
# Obtener máximo del arbol.
# Obtener mínimo del arbol.
# Obtener profundidad del árbol: Altura de la raíz. Deben hacer una operación que calcule la altura de un nodo (del tipo NodoArbol).
# Obtener profundidad de un elemento (Nivel): Recibe un elemento y retorna su profundidad si el elemento esta en el árbol y None en caso contrario.
from graphviz import Digraph
import copy as cp 
class Arbol:
    class Nodo:
        def __init__(self, dato = None, izquierdo = None, derecho = None):
            self.dato = dato
            self.izquierdo = izquierdo
            self.derecho = derecho

        def tieneDerecho(self):
            return self.derecho != None
        
        def tieneIzquierdo(self):
            return self.izquierdo != None
        
        def preOrden(self):
            print(self.dato)
            if self.tieneIzquierdo():
                self.izquierdo.preOrden()
            if self.tieneDerecho():
                self.derecho.preOrden()

        def inOrden(self):
            if self.tieneIzquierdo():
                self.izquierdo.inOrden()
            print(self.dato)
            if self.tieneDerecho():
                self.derecho.inOrden()

        def postOrden(self):
            if self.tieneIzquierdo():
                self.izquierdo.postOrden()
            if self.tieneDerecho():
                self.derecho.postOrden()
            print(self.dato)

        def insertar(self, nuevo):
            if self.dato == nuevo.dato:
                print('El elemento ya esta en el arbol')
            elif nuevo.dato < self.dato:
                if self.tieneIzquierdo():
                    self.izquierdo.insertar(nuevo)
                else:
                    self.izquierdo = nuevo
            else:
                if self.tieneDerecho():
                    self.derecho.insertar(nuevo)
                else:
                    self.derecho = nuevo

        def pertenece(self, datoABuscar):
            if datoABuscar == self.dato:
                return True
            elif datoABuscar < self.dato and self.tieneIzquierdo():
                return self.izquierdo.pertenece(datoABuscar)
            elif datoABuscar > self.dato and self.tieneDerecho():
                return self.derecho.pertenece(datoABuscar)   
            else:
                return False
            
        def esHoja(self):
            return not self.tieneIzquierdo() and not self.tieneDerecho()
        
        def cantidadHojas(self):
            cantidad = 0
            if self.esHoja():
                cantidad += 1
            else:
                if self.tieneIzquierdo():
                    cantidad += self.izquierdo.cantidadHojas()
                if self.tieneDerecho():
                    cantidad += self.derecho.cantidadHojas()
            return cantidad

        def imprimirNodosNivel(self, nivelActual, nivelABuscar):
            if nivelActual == nivelABuscar:
                print(self.dato)
            else:
                if self.tieneIzquierdo():
                    self.izquierdo.imprimirNodosNivel(nivelActual+1, nivelABuscar)
                if self.tieneDerecho():
                    self.derecho.imprimirNodosNivel(nivelActual+1, nivelABuscar)

        def minimo(self):
            if self.tieneIzquierdo():
                return self.izquierdo.minimo()
            else:
                return self.dato
    
        def maximo(self):
            if self.tieneDerecho():
                return self.derecho.maximo()
            else:
                return self.dato
        
        def esAbb(self):
            criterioIzquierdo = True
            criterioDerecho = True
            if self.tieneIzquierdo():
                criterioIzquierdo = self.izquierdo.esAbb() and self.dato > self.izquierdo.maximo()
            
            if self.tieneDerecho():
                criterioDerecho = self.derecho.esAbb() and self.dato < self.derecho.minimo()

            return criterioIzquierdo and criterioDerecho
        
        def eliminar(self, padre, porDonde, dato):
            if self.dato == dato:
                #eliminar hoja
                if self.esHoja():
                    if porDonde == 'Izquierda':
                        padre.izquierdo = None
                    else:
                        padre.derecho = None
                #Si no es hoja, elimino nodo con hijos
                else:
                    if self.tieneIzquierdo():
                        self.dato = self.izquierdo.maximo()
                        self.izquierdo.eliminar(self, 'Izquierda', self.izquierdo.maximo())
                    else:
                        self.dato = self.derecho.minimo()
                        self.derecho.eliminar(self, 'Derecho', self.derecho.minimo())
            else:
                if self.dato < dato:
                    self.derecho.eliminar(self, 'Izquierda', dato)
                else:
                    self.izquierdo.eliminar(self, 'Derecho', dato)
            
        def treePlot(self, dot):
            if self.tieneIzquierdo():
                dot.node(str(self.izquierdo.dato), str(self.izquierdo.dato))
                dot.edge(str(self.dato), str(self.izquierdo.dato))
                self.izquierdo.treePlot(dot)
            else:
                dot.node("-"+str(self.dato)+"l", "-")
                dot.edge(str(self.dato), "-"+str(self.dato)+"l")
            if self.tieneDerecho():
                dot.node(str(self.derecho.dato), str(self.derecho.dato))
                dot.edge(str(self.dato), str(self.derecho.dato))
                self.derecho.treePlot(dot)
            else:
                dot.node("-"+str(self.dato)+"r", "-")
                dot.edge(str(self.dato), "-"+str(self.dato)+"r")
            
    def __init__(self):
        self.raiz = None

    def estaVacio(self):
        return self.raiz == None
    
    def preOrden(self):
        if not self.estaVacio():
            self.raiz.preOrden()
        else:
            print('Arbol vacio')

    def inOrden(self):
        if not self.estaVacio():
            self.raiz.inOrden()
        else:
            print('Arbol vacio')

    def postOrden(self):
        if not self.estaVacio():
            self.raiz.postOrden()
        else:
            print('Arbol vacio')

    def insertar(self, dato):
        nuevoNodo = self.Nodo(dato)
        if self.estaVacio():
            self.raiz = nuevoNodo
        else:
            self.raiz.insertar(nuevoNodo)

    def pertenece(self, datoABuscar):
        if self.estaVacio():
            return False
        else:
            return self.raiz.pertenece(datoABuscar)

    def cantidadHojas(self):
        if self.estaVacio():
            return 0
        else:
            return self.raiz.cantidadHojas()
        
    def imprimirNodosNivel(self,nivelABuscar):
        self.raiz.imprimirNodosNivel(0, nivelABuscar)

    def minimo(self):
        if self.estaVacio():
            print('El arbol esta vacio')
        else:
            return self.raiz.minimo()
    
    def maximo(self):
        if self.estaVacio():
            print('El arbol esta vacio')
        else:
            return self.raiz.maximo()
    
    def esAbb(self):
        if self.estaVacio():
            return True
        else:
            return self.raiz.esAbb()

    def eliminar(self, dato):
        if self.pertenece(dato):
            if self.raiz.dato == dato:
                '''and self.cantidadNodos()  ''' 
                self.raiz = None
            else:
                self.raiz.eliminar(None, ' ', dato)

    def treePlot(self, fileName='arbol'):
      if not self.estaVacio():
        treeDot = Digraph()
        treeDot.node(str(self.raiz.dato), str(self.raiz.dato))
        self.raiz.treePlot(treeDot)
        treeDot.render(fileName, view=True)

arbol = Arbol()
arbol.insertar(50)
arbol.insertar(80)
arbol.insertar(30)
arbol.insertar(10)
arbol.insertar(35)
arbol.insertar(40)
arbol.insertar(60)
arbol.insertar(95)
arbol.insertar(71)
arbol.eliminar(60)

print(arbol.inOrden())


# class ABB:
#   def treePlot(self, fileName='arbol'):
#     if not self.estaVacio():
#       treeDot = Digraph()
#       treeDot.node(str(self.raiz.dato), str(self.raiz.dato))
#       self.raiz.treePlot(treeDot)
#       treeDot.render(fileName, view=True)

#   ##################################################################
#   ##################################################################
#   class __NodoArbol: 
#     def treePlot(self, dot):
#       if self.tieneIzquierdo():
#         dot.node(str(self.izquierdo.dato), str(self.izquierdo.dato))
#         dot.edge(str(self.dato), str(self.izquierdo.dato))
#         self.izquierdo.treePlot(dot)
#       else:
#         dot.node("-"+str(self.dato)+"l", "-")
#         dot.edge(str(self.dato), "-"+str(self.dato)+"l")
#       if self.tieneDerecho():
#         dot.node(str(self.derecho.dato), str(self.derecho.dato))
#         dot.edge(str(self.dato), str(self.derecho.dato))
#         self.derecho.treePlot(dot)
#       else:
#         dot.node("-"+str(self.dato)+"r", "-")
#         dot.edge(str(self.dato), "-"+str(self.dato)+"r")

# Ejercicio 2
# Escribir una operación del TDA ABB que calcule la cantidad de hojas de un árbol.

# [ ]

# Ejercicio 3
# Escribir una operación del TDA ABB que muestre los elementos que estan en el nivel N de un ABB, el nivel se recibe por parámetro.

# [ ]

# Ejercicio 4
# Se define por frontera de un árbol, la secuencia formada por los elementos almacenados en las hojas de un árbol, tomados de izquierda a derecha. Escribir una operación del TDA ABB, que imprima por pantalla la frontera del árbol.

# [ ]

# Ejercicio 5
# Escribir una operación del TDA ABB que retorne una lista ordenada (de menor a mayor) con todos los números pares que forman parte del árbol.

# [ ]

# Ejercicio 6
# Escribir una operación del TDA ABB, que rote el árbol completo, es decir, los elementos del subárbol izquierdo deben ser mayores a la raíz y los del subárbol derecho menores (para todos los nodos del arbol). No se debe retornar un nuevo arbol, sino modificar el arbol desde el que se llama a la operación.

# [ ]
# Ejercicio 7
# Escribir una operación del TDA ABB llamada cantidadNodosEnNivel que retorna la cantidad de nodos del arbol en un nivel determinado