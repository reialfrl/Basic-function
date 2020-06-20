if __name__ == "__main__":

    #Función para calcular el tiempo que tarda la luz del sol a cada planeta
    def distancia_planetas():
        try:
            planeta = input(
                'Ingrese el nombre del planeta con el que desea realizar el calculo:\n\t1)Marte\n\t2)Tierra\n\t3)Venus\n\t4)Mercurio\n')

            if planeta.lower() == 'marte' or (planeta.lower() == 'planeta marte'): distancia = planetas.get('marte')
            elif (planeta.lower() == 'tierra') or (planeta.lower() == 'la tierra') or (planeta.lower() == 'planeta tierra'):
                distancia = planetas.get('tierra')
            elif planeta.lower() == 'venus' or (planeta.lower() == 'planeta venus'): distancia = planetas.get('venus')
            elif planeta.lower() == 'mercurio' or (planeta.lower() == 'planeta mercurio'): distancia = planetas.get('mercurio')

            return print('La luz del sol tarda en llegar a {} aproximadamente {:.2f} minutos'.format(planeta.title(), ((distancia / 299792.458) / 60)))

        except TypeError:
            print('El valor ingresado es incorrecto o el planeta ingresado no se encuentra en las opciones')        

        except UnboundLocalError:
            print('El valor ingresado es incorrecto o el planeta ingresado no se encuentra en las opciones')        

    planetas = {'marte': 227940000, 'tierra': 146600000,
                'venus': 108200000, 'mercurio': 57910000}
