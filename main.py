import flet as ft
import random
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

    ordenamiento(row.controls, page)


ft.app(target=main)
