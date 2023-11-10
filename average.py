def average(*numeros):
    """Funcion que obtiene el promedio."""

    suma = 0

    for number in numeros:
        suma = number + suma

    media = suma / (len(numeros))

    return media

print(average(2,4,8))