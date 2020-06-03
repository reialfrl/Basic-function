def cantidad_digitos(numero):
    digitos = 0

    while numero > 0:
        numero = numero // 10
        digitos += 1

    return digitos

digitos = cantidad_digitos(10)
print(digitos)
