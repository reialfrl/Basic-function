if __name__ == "__main__":
    #Función para convertir los grados centigrados ingresados por el usuario a grados fahrenheit
    def grados_fahrenheit():
        try:
            centigrados = float(input('Ingrese la cantidad de grados centigrados que desea convertir: '))
            if centigrados <= 0:
                print('El valor ingresado debe ser mayor a 0 o un numero positivo')
            else:
                return print(f'{centigrados} ºC son: {(centigrados * 9 / 5) + 32} ºF')
        except ValueError:
            print('El dato que ingreso es incorrecto, solo se aceptan numeros positivos')tivos')
