if __name__ == "__main__":
    #Función para convertir los grados centigrados ingresados por el usuario a grados fahrenheit
    def grados_fahrenheit(centigrados):
        if centigrados <= 0:
            print('El valor ingresado debe ser mayor a 0 o un numero positivo')
        return (centigrados * 9 / 5) + 32

    try:
        centigrados = float(
            input('Ingrese la cantidad de grados centigrados que desea convertir:\n'))
        total = grados_fahrenheit(centigrados)
        print(f'{centigrados} ºC son:\n{total} ºF')
    except ValueError:
        print('El dato que ingreso es incorrecto, solo se aceptan numeros positivos')
