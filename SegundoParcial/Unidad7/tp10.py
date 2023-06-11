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
# [ ]
# from graphviz import Digraph
# import copy as cp 

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