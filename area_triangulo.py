if __name__ == "__main__":
    #Función para calcular el area de un triangulo
    def area():
        try:
            base = float(input('Ingrese el valor de la base de su triangulo: '))
            altura = float(input('Ingrese el valor de la altura de su triangulo: '))
            if (base <= 0) or (altura <= 0):
                print('El valor ingresado debe ser mayor a 0 o un numero positivo')
            else:
                return (f'La base de su triangulo es de {(base * altura) / 2}')
        except ValueError:
            print('El dato que ingreso es incorrecto, solo se aceptan numeros positivos')
