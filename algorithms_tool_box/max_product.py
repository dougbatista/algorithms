def maxProduct(arr, n):

    # Valida se existem pares
    if (n < 2):
        print("There are no pairs")
        return 0

    arr.sort()

    # Inicializa os pares
    # a = arr[0]
    # b = arr[1]
    result = 0

    # Solução rapida se houver o sort da lista
    result = arr[len(arr) - 1] * arr[len(arr) - 2]

    # Percorrendo todos os pares possíveis
    # Guardando todos os pares.
    # for i in range(n):
    #     for j in range(i + 1, n):
    #         if (arr[i] * arr[j] > a * b):
    #             result = arr[i] * arr[j]

    return result


def colect_data():
    raw_n_elements = input()
    raw_arr_values = input().split()

    arr_values = [0] * len(len(raw_arr_values))
    n_elements = int(raw_n_elements)

    for i in range(0, len(raw_arr_values)):
        arr_values[i] = int(raw_arr_values[i])

    return arr_values, n_elements


def main():
    arr, n = colect_data()
    result = maxProduct(arr, n)
    print(result)


main()
