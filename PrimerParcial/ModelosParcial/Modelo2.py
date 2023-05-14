'''
Escribir una funcion recursiva tieneRepetidos(arreglo) que recibe un arreglo de 
numeros enteros ordenado y retorna verdadero si tiene al menos un numero repetido.
Suponer que el arreglo NO esta vacio
'''
arregloRepetido = [1, 2, 3, 4, 5, 3]
arregloNoRepetido = [1, 2, 3, 4, 5, 6]

def tieneRepetidos(arreglo, indice):
    resultado = False
    if indice == 0:
        resultado = repetidoAux(arreglo[indice], arreglo)
    else:
        resultado = tieneRepetidos(arreglo, indice-1) or repetidoAux(arreglo[indice], arreglo)

    return resultado

def repetidoAux(elemento, arreglo):
    resultado = False
    contador = 0
    for indice in range(len(arreglo)):
        if arreglo[indice] == elemento:
            contador +=1
            if contador>=2:
                resultado = True

    return resultado

'''TDA'''

class Expediente:
    def __init__(self, id, urgencia = False, aJuicio = False):
        self.id = id
        self.urgente = urgencia
        self.aJuicio = aJuicio

    def __repr__(self):
        return f"Expediente(id= {self.id}, urgente= {self.urgente}, aJuicio= {self.aJuicio})"


class Pila:
   def __init__(self, lista):
      self.estructura = lista

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

class Juzgado:
    def __init__(self, expedientesUrgentes, expedientesNormales, nroJuzgado:int, cantidadCritica:int = 50):
       self.expedientesUrgentes = expedientesUrgentes
       self.expedientesNormales = expedientesNormales
       self.nroJuzgado = nroJuzgado
       self.cantidadCritica = cantidadCritica
    
    def __repr__(self):
        return f"Juzgado(nroJuzgado={self.nroJuzgado}, expedientesUrgentes={self.expedientesUrgentes.__repr__()}, expedientesNormales={self.expedientesNormales.__repr__()})"

    def ingresarExpediente(self, expediente:Expediente):
        if expediente.urgente:
            self.expedientesUrgentes.apilarElemento(expediente)
        else:
           self.expedientesNormales.apilarElemento(expediente)

    def primerExpedienteATratar(self):
       if not self.expedientesUrgentes.estaVacia():
          return self.expedientesUrgentes.primerElemento()
       else:
          return self.expedientesNormales.primerElemento()
    
    def esCritico(self):
       return self.expedientesUrgentes.tamaño()> self.cantidadCritica or self.expedientesNormales.tamaño()> self.cantidadCritica

# Creamos los expedientes
expediente1 = Expediente(1, True, False)  # Urgente
expediente2 = Expediente(2, False, False) # Normal
expediente3 = Expediente(3, True, False) # Urgente
expediente4 = Expediente(4, True, False) # Urgente
# Creamos el juzgado
juzgado = Juzgado(Pila([]), Pila([]), 1, 1)

# Ingresamos los expedientes al juzgado
juzgado.ingresarExpediente(expediente1)
juzgado.ingresarExpediente(expediente2)
juzgado.ingresarExpediente(expediente3)
juzgado.ingresarExpediente(expediente4)

# Obtenemos el primer expediente a tratar
primer_expediente = juzgado.primerExpedienteATratar()
print("Primer expediente a tratar:", primer_expediente.id)

# Verificamos si el juzgado es crítico
print("¿Es crítico el juzgado?", juzgado.esCritico())

print(juzgado)
