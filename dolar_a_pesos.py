if __name__ == "__main__":
    #Función para convertir dolares a pesos colombianos
    def convertir(dolares):
        pesos_colombianos = 3775.03
        if dolares <= 0:
            print('El valor ingresado debe ser mayor a 0 o un numero positivo')
        else:
            return dolares * pesos_colombianos

    try:
        dolares = float(input('Ingrese la cantidad de Dolares que desea convertir a Pesos Colombianos:\n'))
        total = convertir(dolares)
        print(f'{dolares} Dolares son:\n{total} Pesos Colombianos')
    except ValueError:
        print('El dato que ingreso es incorrecto, solo se aceptan numeros positivos')
