def creacion_listas():
    try:
        longitud1 = int(input('Ingresa la longitud de la primera lista: '))
        lista_final1 = [int(input('Ingresa un número a la lista: ')) for _ in range(longitud1)]
        longitud2 = int(input('Ingresa la longitud de la segunda lista: '))
        lista_final2 = [int(input('Ingresa un número a la lista: ')) for _ in range(longitud2)]        
        return lista_final1, lista_final2
    except ValueError:
        print('Debe ingresar un número entero positivo')


