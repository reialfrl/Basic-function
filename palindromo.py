def palindromo(sentencia):
    sentencia = sentencia.lower().replace(' ', '')

    return sentencia == sentencia[::-1]
