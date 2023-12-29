import flet as ft
import time


def ordenamiento(arr: list, page: ft.Page):
    n = len(arr)
    for iteracion in range(n):
        for posicion in range(0, n - iteracion - 1):

            arr[posicion].bgcolor = ft.colors.YELLOW
            arr[posicion + 1].bgcolor = ft.colors.YELLOW
            time.sleep(0.5)
            page.update()
            if int(arr[posicion].content.value) > int(arr[posicion + 1].content.value):
                arr[posicion], arr[posicion + 1] = arr[posicion + 1], arr[posicion]

            arr[posicion].bgcolor = ft.colors.ORANGE
            arr[posicion + 1].bgcolor = ft.colors.ORANGE
        arr[n - iteracion - 1].bgcolor = ft.colors.GREEN
    page.update()
