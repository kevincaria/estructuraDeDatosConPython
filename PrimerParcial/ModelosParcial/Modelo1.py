import numpy as np

# Ejercicio1
# Escribir la función recursivaincluido(arr1, arr2) que retorna verdadero si arr1 está
# incluido en arr2.
# Donde estar incluido significa que todos los elementos de arr1 están en alguna posición de arr2.
# Ayuda: Hacer primero la función auxiliar incluidoAux(elem, arr3) devuelve verdadero si
# elem está en arr3. Esta función puede no ser recursiva.
vector = np.array([12, 13, 14])
vector2 = np.array([2, 4, 1, 2, 7, 9])
def recursivaincluido(primerArreglo, indice, segundoArreglo):
    resultado = False
    if indice == 0:
        resultado = incluidoAux(primerArreglo[indice], segundoArreglo)
    else:
        resultado = recursivaincluido(primerArreglo, indice-1,segundoArreglo) and incluidoAux(primerArreglo[indice], segundoArreglo)


def incluidoAux(elemento, arreglo):
    resultado = False
    for indice in range(len(arreglo)):
        if arreglo[indice] == elemento:
            resultado = True

    return resultado

# Ejercicio2
# La unaHur nos pidió ayuda para administrar los laboratorios del campus.
# Se debe iniciar el TAD Laboratorios con la cantidad de laboratorios disponibles, cosa que no va a
# cambiar.
# Cada laboratorio tiene una cantidad de computadoras, una cantidad de sillas y si tiene ventanas o no.
# Se recomienda crear primero el TAD Laboratorio.
# Implementar al menos las siguientes operaciones del TAD Laboratorios:

# definirLaboratorio(indiceLabororatorio, cantCompus, cantVentanas)
# donde el índice está entre 0 y la cantidad de laboratorios con que se inicializó.
# Si el laboratorio ya existía, se tiene que redefinir(modificar).

# laboratorioConMasVentanas()
# que devuelve el laboratorio con más ventanas. Notar que no necesariamente están todos los
# laboratorios definidos.

# vaciarLaboraratorios()
# que elimina los laboratorios definidos

# ¡No son las únicas operaciones necesarias, agregar los métodos que crean necesarios, como el
# constructor!

class Campus:
    def __init__(self, cantidad):
        self.laboratorios = np.zeros(cantidad,Laboratorio)

    def __repr__(self):
        return
    
    def definirLaboratorio(self, indiceLaboratorio, cantCompus, cantSillas, cantVentanas):
        self.laboratorios[indiceLaboratorio] = Laboratorio(indiceLaboratorio, cantCompus, cantSillas, cantVentanas)
    
    def laboratorioConMasVentanas(self):
        maximo = self.laboratorios[0]
        for i in range(len(self.laboratorios)):
            if self.laboratorios[i] != 0:
                if self.laboratorios[i].ventanas > maximo.ventanas:
                    maximo = self.laboratorios[i]
        return maximo
    
    def vaciarLaboraratorios(self):
        for i in range(len(self.laboratorios)):
            self.laboratorios[i] = 0

class Laboratorio:
    def __init__(self, id, computadoras = 0, sillas = 0, ventanas = 0):
        self.id = id
        self.computadoras = computadoras
        self.sillas = sillas
        self. ventanas = ventanas
    
    def __repr__(self):
        return (f'ID: {self.id}\n Cantidad de computadoras: {self.computadoras} Cantidad de sillas: {self.sillas} Cantidad de ventadas: {self.ventanas}')

    
laboratorios = Campus(2)
laboratorios.definirLaboratorio(0, 2, 3, 50)
laboratorios.definirLaboratorio(1, 2, 2, 15)
laboratorios.definirLaboratorio(1, 2, 2, 30)
print(laboratorios)