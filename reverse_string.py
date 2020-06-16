#Representacion inversa de una cadena de string
def reverse_string(cadena):
    try:
        return cadena[::-1]
    except TypeError:
        print('Solo puede ingresar cadenas de caracteres')