def factorial(valor):
    if (valor == 1):
        return valor
    else:
        return valor * factorial(valor - 1)

print("El factorial es:", factorial(10))
