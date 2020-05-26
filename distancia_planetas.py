if __name__ == "__main__":

    planetas = {'marte': 227940000, 'tierra': 146600000,
                'venus': 108200000, 'mercurio': 57910000}
 
    #Función para calcular el tiempo que tarda la luz del sol a cada planeta
    def distancia_planetas(planeta):
        if planeta.lower() == 'marte' or (planeta.lower() == 'planeta marte'):
            planeta = planetas.get('marte')
        elif (planeta.lower() == 'tierra') or (planeta.lower() == 'la tierra') or (planeta.lower() == 'planeta tierra'):
            planeta = planetas.get('tierra')
        elif planeta.lower() == 'venus' or (planeta.lower() == 'planeta venus'):
            planeta = planetas.get('venus')
        elif planeta.lower() == 'mercurio' or (planeta.lower() == 'planeta mercurio'):
            planeta = planetas.get('mercurio')
        else:
            planeta == int
        return (planeta / 299792.458) / 60
    try:
        planeta = input(
            'Ingrese el nombre del planeta con el que desea realizar el calculo:\n\t1)Marte\n\t2)Tierra\n\t3)Venus\n\t4)Mercurio\n')
        tiempo = distancia_planetas(planeta)
        print(f'La luz del sol tarda en llegar a {planeta.title()} aproximadamente {round(tiempo, 2)} minutos')
    except TypeError:
        print('El valor ingresado es incorrecto o el planeta ingresado no se encuentra en las opciones')
