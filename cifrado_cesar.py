import string 

def cifrado(sentencia, llave=10):
    sentencia = sentencia.lower()
    alfabeto = string.ascii_lowercase
    size_alfabeto = len(alfabeto)
    cifrado = ''

    for letra in sentencia:

        if letra in alfabeto:
            nuevo_indice = (alfabeto.index(letra) + llave )
            cifrado += alfabeto[nuevo_indice % size_alfabeto]
        else:
            cifrado += letra

    return cifrado
                       

a = cifrado('Hola Como estaz', 23)
print(a)
        

def descifrado(sentencia, llave=10):
    sentencia = sentencia.lower()
    alfabeto = string.ascii_lowercase
    size_alfabeto = len(alfabeto)
    cifrado = ''

    for letra in sentencia:

        if letra in alfabeto:
            nuevo_indice = (alfabeto.index(letra) - llave)
            cifrado += alfabeto[nuevo_indice % size_alfabeto]
        else:
            cifrado += letra

    return cifrado


a = descifrado('elix zljl bpqxw', 23)
print(a)
    
