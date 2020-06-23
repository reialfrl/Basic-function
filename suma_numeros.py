def suma_numeros(a, b, c): 
    '''
    Calcula la suma de los tres argumentos
    Si los tres argumentos son iguales se multiplican por tres
    '''
    suma = a + b + c

    if a == b and a == c: suma *= 3

    return suma
   