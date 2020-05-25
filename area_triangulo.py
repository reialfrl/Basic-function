if __name__ == "__main__":
    #Función para calcular el area de un triangulo
    def area(base, altura):
        if (base <= 0) or (altura <= 0):
            print('El valor ingresado debe ser mayor a 0 o un numero positivo')
        else:
            return (base * altura) / 2

    try:
        base = float(input('Ingrese el valor de la base de su triangulo: '))
        altura = float(input('Ingrese el valor de la altura de su triangulo: '))
        total = area(base, altura)
        print(f'La base de su triangulo es de {total}')
    except ValueError:
        print('El dato que ingreso es incorrecto, solo se aceptan numeros positivos')
