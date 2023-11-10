mylist = [3,3,2,1,5,8,99]

def median(list_numbers):
    """This function calculate the median."""

    # Organizo la lista.
    sorted_list = sorted(list_numbers)

    # Si la cantidad de números de la lista es par.
    if len(sorted_list) % 2 == 0:
        ind_base = (len(sorted_list)/2) - 1  # Calculo el índice base. Resto uno, ya que la listas el primer valor es 0.
        ind_next = (len(sorted_list)/2)      # Obtengo el segundo indice base.

        value1 = sorted_list[int(ind_base)]  # Transformo el tipo de datos a integer.
        value2 = sorted_list[int(ind_next)]

        result = (value1 + value2) / 2      # Obtengo el resultado.

        return result

    # Si la cantidad de números de la lista es impar.
    else:
        add_index = len(sorted_list) + 1   # Añado un uno a la cantidad total de números que contiene la lista.
        ind_base = (add_index/2) - 1       # Resto uno al resultado, ya que los índices comienzan por cero.
        result = sorted_list[int(ind_base)]
        return result

print(median(mylist))
