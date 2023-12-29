import flet as ft
import random
import time
from algoritmo import ordenamiento


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def create_container(number: int) -> list:
        """Creación de contenedores que simulan el dato."""
        container_list = []
        for _ in range(number):
            container_list.append(
                ft.Container(
                    content=ft.Text(value=str(random.randint(1, 100)), color=ft.colors.BLACK),
                    alignment=ft.alignment.center,
                    width=50,
                    height=50,
                    bgcolor=ft.colors.ORANGE,
                    border_radius=25
                )
            )
        return container_list

    row = ft.Row(controls=create_container(10), alignment=ft.MainAxisAlignment.CENTER)

    page.add(row)

    arr = row.controls
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
    print(arr)


ft.app(target=main)
