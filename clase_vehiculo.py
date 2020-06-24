class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas)

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas) 
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + ", {} kg de peso".format(self.carga)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ", {}".format(self.tipo)

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

def catalogar(lista, ruedas=None):
    #Función que muestra los vehiculos según su número de ruedas, en caso de que el valor de ruedas sea None, muestra todo.
    if ruedas != None:
        contador = 0
        for v in vehiculos:
            if v.ruedas == ruedas:
                contador += 1
        print("Se han encontrado {} vehículos con {} ruedas".format(contador, ruedas))
        print('--------------------------------------------------------------')

    for v in lista:
        if ruedas == None:
            print('{} {}'.format(type(v).__name__, v))
        elif v.ruedas == ruedas:
            print('{} {}'.format(type(v).__name__, v))

vehiculos = [
    Coche('Azul', 4, 150, 1200),
    Camioneta('Blanco', 4, 100, 1300, 1500),
    Bicicleta('Verde', 2, 'Urbana'),
    Motocicleta('Negro', 2, 'Deportiva', 180, 900)
]

catalogar(vehiculos, 2)
