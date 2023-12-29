def ordenamiento(arr: list):
    n = len(arr)
    for iteracion in range(n):
        for posicion in range(0, n - iteracion - 1):
            if arr[posicion] > arr[posicion + 1]:
                arr[posicion], arr[posicion + 1] = arr[posicion + 1], arr[posicion]


