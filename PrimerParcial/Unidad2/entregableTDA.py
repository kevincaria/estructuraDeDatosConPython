'''
Entregable TDA

Formato de entrega: Se entrega en papel manuscrito, en imprenta, escribiendo el nombre
en cada hoja. La entrega es obligatoria para poder rendir el parcial.
Atención: No es obligatorio aprobar esta entrega para poder rendir el parcial
Consigna: Se debe modelar el TDA que surge del enunciado. Es decir, explicar la interfaz a
utilizar que modele el enunciado. Luego se debe implementar en papel.

Enunciado

La unaHur nos pidió ayuda para administrar el bar (TDA Bar).
El bar tiene tres menús:
El menú estudiantil vale $200.
El menú docente vale $300.
El menú general vale $400.

Durante el día la gente va pidiendo menúes indicando que tipo de menú va a pedir. No nos
interesa modelar la gente, sino que menús pide.

En algún momento el bar quiere saber cuánta plata lleva recaudada. 

También se tiene que poder resetear la cuenta para comenzar de nuevo.

No son las únicas operaciones necesarias, agregar las operaciones y funciones que
consideren necesarios, como el constructor (__init__()).

Por ejemplo:
Si dos estudiantes y tres docentes pidieron un menú, la plata recaudada debería ser $1300.
'''
def validarTipo(tda, atributo, tipo, condicion = True, explicacion = ''):
    if type(tda) == tipo and condicion:
        return tda
    else:
        raise Exception(f'La variable {atributo} debe ser {str(tipo)} {explicacion}')
    
class Bar():
    def __init__(self, estudiantil = 200.00, docente = 300.00, general = 400.00, cantidadEstudiantil = 0, cantidadDocente = 0, cantidadGeneral = 0):  
        self.estudiantil = validarTipo(estudiantil, 'estudiantil', float, estudiantil >= 0, 'o se ingreso un monto menor a 0')
        self.docente = validarTipo(docente, 'docente', float, docente >= 0, 'o se ingreso un monto menor a 0')
        self.general = validarTipo(general, 'general', float, general >= 0, 'o se ingreso un monto menor a 0')
        self.cantidadEstudiantil = validarTipo(cantidadEstudiantil, 'cantidadEstudiantil', int, cantidadEstudiantil >= 0, 'o se ingreso una cantidad menor a 0')
        self.cantidadDocente = validarTipo(cantidadDocente, 'cantidadDocente', int, cantidadDocente >= 0, 'o se ingreso una cantidad menor a 0')
        self.cantidadGeneral = validarTipo(cantidadGeneral, 'cantidadGeneral', int, cantidadGeneral >= 0, 'o se ingreso una cantidad menor a 0')

    def __repr__(self):
        return(f'     Menu\nEstudiantil: ${str(self.estudiantil)} \nDocente: ${str(self.docente)}\nGeneral: ${self.general}\n \n     Cantidades vendidas\nEstudiantil: {str(self.cantidadEstudiantil)}\nDocente: {str(self.cantidadDocente)}\nGeneral: {str(self.cantidadGeneral)}')  
    
    def facturarEstudiantil(self, cantidad = 1):
        self.cantidadEstudiantil += validarTipo(cantidad, 'cantidad', int, cantidad >= 0, 'o se ingreso una cantidad menor a 0')

    def facturarDocente(self, cantidad = 1):
        self.cantidadDocente += validarTipo(cantidad, 'cantidad', int, cantidad >= 0, 'o se ingreso una cantidad menor a 0')

    def facturarGeneral(self, cantidad = 1):
        self.cantidadGeneral += validarTipo(cantidad, 'cantidad', int, cantidad >= 0, 'o se ingreso una cantidad menor a 0')

    def actualizarMenuEstudiantil(self, precio):
        self.estudiantil = validarTipo(precio, 'general', float, precio >= 0, 'o se ingreso un monto menor a 0')

    def actualizarMenuDocente(self, precio):
        self.docente = validarTipo(precio, 'general', float, precio >= 0, 'o se ingreso un monto menor a 0')

    def actualizarMenuGeneral(self, precio):
        self.general = validarTipo(precio, 'general', float, precio >= 0, 'o se ingreso un monto menor a 0')

    def recaudacionActual(self):
        recaudacion = self.estudiantil*self.cantidadEstudiantil + self.docente*self.cantidadDocente + self.general*self.cantidadGeneral
        return (f'La recaudacion actual es de ${str(recaudacion)}')
    
    def resetearRecaudacion(self):
        self.cantidadEstudiantil = 0
        self.cantidadDocente = 0
        self.cantidadGeneral = 0
    
bar = Bar()


bar.facturarDocente()
bar.facturarEstudiantil()
print(bar)
print(bar.recaudacionActual())
bar.resetearRecaudacion()
print(bar)
print(bar.recaudacionActual())