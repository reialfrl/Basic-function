#Area de un circulo
from math import pi

def circle_area(radio):
    try:
        radio = float(input('Ingrese el radio del circulo: '))
        return print('El area del circulo segun el radio de {} es de {:.2f}'.format(radio, (pi * radio**2)))
    except ValueError:
        print('El valor ingresado debe ser un número')    

