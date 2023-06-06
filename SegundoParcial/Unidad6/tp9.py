class Lista:
    class Nodo:
        def __init__(self,valor):
            self.valor = valor
            self.siguiente = None
            
        def __repr__(self):
            return ':' + self.valor.__repr__()
        
        def tamañoNodo(self):
            if self.siguiente == None:
                return 1
            else:
                return 1 + self.siguiente.tamañoNodo()
            
        def insertarNodo(self, nuevo):
            if self.siguiente == None:
                self.siguiente = nuevo
            else:
                self.siguiente.insertarNodo(nuevo)

    def __init__(self):
        self.tamaño = 0
        self.primero= None

    def tamaño(self): #ESTA MAL
        ret = 0
        if self.primero != None:
            ret = self.primero.tamañoNodo()
        return ret
    
        # if self.primero == None:
        #     return 0
        # else:
        #     return self.primero.tamañoNodo()

    def insertar(self, elemento):
        nuevo = self.Nodo(elemento)

        if self.tamaño == 0:
            self.primero = nuevo
        else: 
            self.primero.insertarNodo(nuevo)
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
        
lista = Lista()
lista.insertar(1)
lista.insertar(5)
print(lista)