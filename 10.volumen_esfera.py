from math import pi

def volumen_esfera():
    r = float(input('Ingrese el radio de la esfera: ') )

    volumen = 4/3 * pi * r **3

    return print('El volumen de la esfera es {:.2f} unidades cúbicas'.format(volumen))

