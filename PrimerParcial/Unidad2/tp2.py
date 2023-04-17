'''
Ejercicio 1
Implementar el TDA "Propiedad" que modela un inmueble, con una estructura definida por 
los siguientes componentes:

Calle
Número
Localidad
Año de construcción
Cantidad de ambientes
Implementar las siguientes operaciones:

Constructor: Debe incluir las validaciones necesarias, teniendo en cuenta que solo se almacenan 
propiedades construidas luego de 1870.

__repr__: Al usar la función print con una variable del tipo propiedad debe mostrar: 
'calle' 'numero' ('localidad').

mismaLocalidad: Operación que recibe dos propiedades y retorna True si estan en la misma localidad 
y False en caso contrario.

mayorNumeración: Operación que recibe dos propiedades y si están en la misma calle, 
retorna la que posee mayor numeración. Si están calles diferentes debe lanzar una excepción.

calculaImpuestoARBA: Operación que retorna el porcentaje de impuesto inmobiliario de una propiedad, 
según la siguiente regla:

Propiedades entre 1870 y 1949:

Entre 1 y 3 ambientes: 5% de impuesto
Entre 4 y 6 ambientes: 10% de impuesto
Más de 6 ambientes: 25 % de impuesto

Propiedades desde 1950 hasta la actualidad:
Entre 1 y 5 ambientes: 5% de impuesto
Más de 5 ambientes: 35 % de impuesto
'''
class Propiedad:
    def __init__(self, calle = '', numero = 0, localidad = '', año = 1871, ambientes = 0):

        if type(calle) == str:
            self.calle = calle.title()
        else:
            raise Exception('La calle ingresada tiene un formato inválido')
        
        if type(numero) == int and numero > 0:
            self.numero = numero
        else:
            raise Exception('La calle ingresada tiene un formato inválido o es menor a 0')
        
        if type(localidad) == str:
            self.localidad = localidad.title()
        else:
            raise Exception('La localidad ingresada tiene un formato inválido')
        
        if type(año) == int and año>= 1871:
            self.año = año
        else:
            raise Exception('El año ingresado tiene un formato inválido o es menor a 1870')
        
        if type(ambientes) == int and ambientes > 0:
            self.ambientes = ambientes
        else:
            raise Exception('La calle ingresada tiene un formato inválido o es menor a 0')
    
    def __repr__(self):
        return (f'{self.calle} {str(self.numero)} ({self.localidad})')
    
    def mismaLocalidad(self, propiedad):
        return self.localidad == propiedad.localidad
    
    def mayorNumeracion(self, propiedad):
        if self.calle == propiedad.calle:
            if max(self.numero, propiedad.numero) == self.numero:
                return self
            else:
                return propiedad
        else:
            raise Exception('Las propiedades no son de la misma calle')

    def impuestoPropiedadAntigua(ambientes):
        impuesto = 0

        if ambientes >= 3:
            impuesto = 5
        elif ambientes >= 4 and ambientes <=6:
            impuesto = 10
        else:
            impuesto = 25
        
        return impuesto

    def impuestoPropiedadActual(ambientes):
        impuesto = 0

        if ambientes >= 5:
            impuesto = 5
        else:
            impuesto = 35
        
        return impuesto
    
    def calculaImpuestoARBA(self):
        impuesto = 0
        if self.año <= 1949 :
            impuesto = self.impuestoPropiedadAntigua(self.ambientes)
        else:
            impuesto = self.impuestoPropiedadActual(self.ambientes) 
        
        return(f'{str(impuesto)}% de impuesto')
        
propiedad1 = Propiedad('vergara', 10, 'moron', 1890, 3)
propiedad2 = Propiedad ('vergara', 5, 'moron', 1990, 5)

print(propiedad1.mayorNumeracion(propiedad2))

'''
Ejercicio 2
Implementar el TDA "Quiniela" que modela un juego de quiniela con dos números premiados. 
La estructura contiene:

Primer número premiado
Segundo número premiado
Multiplicador (cuánto se paga por cada peso apostado)
Implementar las siguientes operaciones:

Constructor: Debe incluir las validaciones necesarias, teniendo en cuenta que los números que 
participan se encuentran entre 0 y 999.192.168.129.123:5672

__repr__: Al usar la función print con una variable del tipo quiniela debe mostrar: 
Primer número ganador: 'numero' - Segundo número ganador: 'numero' - Paga: 'multiplicador'X.

esNumeroGanador: Operación que recibe un número por parámetros y retorna True si el número 
resultó ganador o False en caso contrario.

importeAPagar: Operación que recibe un número y el monto apostado por parámetros y retorna el 
importe a pagar si la apuesta es ganadora o 0 en caso contrario. Si el número es el primer premio, 
se paga 'mutiplicador' por cada peso apostado, si es el segundo premio se paga la mitad. 
Solo se aceptan apuestas hasta $1000.

premiadosCercanos: Operación que retorna True si los números premiados están a menos de 
10 números de distancia y False en caso contrario.
'''
def validarTipo(tda, atributo, tipo, condicion = True, explicacion = ''):
    if type(tda) == tipo and condicion:
        return tda
    else:
        raise Exception(f'La variable {atributo} debe ser {str(tipo)} {explicacion}')
class Quiniela:
    def __init__(self, primerPremio, segundoPremio, multiplicador):
        self.primerPremio = validarTipo(primerPremio,'El primer Premio', int, primerPremio > 0, 'o se ingreso un numero negativo')
        self.segundoPremio = validarTipo(segundoPremio,'El segundo Premio', int, segundoPremio > 0, 'o se ingreso un numero negativo')
        self.multiplicador = validarTipo(multiplicador,'El multiplicador', int, multiplicador > 0, 'o se ingreso un numero negativo')

# __repr__: Al usar la función print con una variable del tipo quiniela debe mostrar: 
# Primer número ganador: 'numero' - Segundo número ganador: 'numero' - Paga: 'multiplicador'X.
    def __repr__(self):
        return (f'Primer número ganador: {str(self.primerPremio)} - Segundo número ganador: {str(self.segundoPremio)} - Paga: {str(self.multiplicador)}X.')

# esNumeroGanador: Operación que recibe un número por parámetros y retorna True si el número 
# resultó ganador o False en caso contrario.
    def esNumeroGanador(self, numero):
        return self.primerPremio == numero or self.segundoPremio == numero
    
# importeAPagar: Operación que recibe un número y el monto apostado por parámetros y retorna el 
# importe a pagar si la apuesta es ganadora o 0 en caso contrario. Si el número es el primer premio, 
# se paga 'mutiplicador' por cada peso apostado, si es el segundo premio se paga la mitad. 
# Solo se aceptan apuestas hasta $1000.
    def importeAPagar(self, numero, monto):
        
        premio = 0

        if self.esNumeroGanador(numero):
            if(self.primerPremio == numero):
                premio = monto*self.multiplicador
            else:
                premio = (monto*self.multiplicador)/2
        else:
            premio = 0

        return premio
            
# premiadosCercanos: Operación que retorna True si los números premiados están a menos de 
# 10 números de distancia y False en caso contrario.
    def premiadosCercanos(self):
        return abs(self.primerPremio - self.segundoPremio) < 10
'''
Ejercicio 3
Implementar el TDA "Cuenta" que modela una cuenta bancaria, la estructura de datos esta 
compuesta por los siguientes componentes:

Número de cuenta
DNI del titular
Saldo de cuenta actual
Interés anual
Implementar las siguientes operaciones:

Constructor: Debe incluir las validaciones necesarias.
__repr__: Al usar la función print con una variable del tipo cuenta debe mostrar: 
Cuenta Nro: 'numero' - Titular: 'dni' ($'saldo').

ingresarDinero: Operación que recibe un número e ingresa esa cantidad en la cuenta.

actualizarSaldo: Operación que actualiza el saldo de la cuenta aplicándole el interés diario 
(interés anual dividido entre 365).

retirarDinero: Operación que recibe un número y extrae esa cantidad de la cuenta 
(si hay saldo disponible), sino debe lanzar una excepción.
'''
class Cuenta:
    def __init__(self, nroCuenta, dni, saldoInicial, interesAnual):
        self.nroCuenta = validarTipo(nroCuenta, 'nroCuenta', int, nroCuenta > 0, 'o el nro de cuenta ingresado fue negativo')
        self.dni = validarTipo(dni, 'dni', int, dni > 0, 'o el numero de dni ingresado fue menor a 0')
        self.saldo = validarTipo(saldoInicial, 'saldoInicial', float, saldo > 0, ' o el saldo ingresado fue negativo') 
        self.interesAnual = validarTipo(interesAnual, 'interesAnual', float, interesAnual > 0, 'o el interes anual ingresado fue negativo')

    def __repr__(self):
        return (f'Cuenta Nro: {str(self.nroCuenta)} - Titular: {str(self.dni)} (${str(self.saldo)})')
    
    #Se asume que esta funcion tiene que actualizarse manualmente, 
    # por lo que se actualiza con el interes correspondiente a la cantidad de dias pasados por parametro
    def actualizarSaldo(self, dias): 
        interesAplicado = (self.interesAnual/365)*dias
        self.saldo += (self.saldo*interesAplicado)

    def ingresarDinero(self, saldo):
        self.saldo += saldo

    def retirarDinero(self, retiro):
        if self.saldo >= retiro :
            self.saldo -= retiro
        else:
            raise Exception('La cantidad de dinero que desea retirar es mayor al saldo actual de la cuenta')

'''
Ejercicio 4
Implementar el TDA "Tiempo" que modela una duracion en horas, minutos y segundos.

Se deben implementar las siguientes operaciones:

Constructor: Debe incluir las validaciones necesarias, la hora debe ser un número positivo y 
los minutos y segundos deben ser números positivos entre 0 y 59.

__repr__: Al usar la función print con una variable del tipo tiempo debe mostrar: 
'horas':'minutos':'segundos'.

tiempoASegundos: Operación que toma una variable de tipo tiempo y retorna la cantidad en segundos.

tiemposDesdeSegundos: Operación que recibe un tiempo en segundos como parámetro y 
retorna una variable de tipo tiempo, en horas minutos y segundos.

mayorDuracion: Operación que recibe dos variables de tipo tiempo y retorna la de mayor duración.
'''

'''
Ejercicio 5
Las plataformas de música online como YouTube y Spotify almacenan la información asociada 
a las canciones en estructuras de datos complejas para hacer las búsquedas de manera eficiente. 
Para esto se deben modelar las canciones. Implementar el TDA "Cancion" con 
los siguientes componentes:

Nombre
Artista
Duración
Género musical (6 posibles: Rock, Jazz, Blues, Funk, Reggae y Rap).
Año de edición
Número de likes

Implementar las siguientes operaciones:

Constructor: Debe incluir las validaciones necesarias.

__repr__: Al usar la función print con una variable del tipo canción debe mostrar: 
'nombre' - 'artista' ('duracion').

mayorDuracion: Operación que recibe dos canciones por parámetros y retorna la de mayor duración.

agregaLikes: Operación que recibe un número e incrementa la cantidad de likes de la canción en 
ese número.

masVotada: Operacion que recibe dos canciones y sin son del mismo artista y 
del mismo género musical, retorna la que tiene mayor cantidad de likes. 
En caso contrario debe lanzar una excepción.
'''