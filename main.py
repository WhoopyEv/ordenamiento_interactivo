import flet as ft


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def create_container(number: int) -> list:
        """Creación de contenedores que simulan el dato."""
        container_list = []
        for _ in range(number):
            container_list.append(
                ft.Container(
                    content=ft.Text(),
                    alignment=ft.alignment.center,
                    width=50,
                    height=50,
                    bgcolor=ft.colors.ORANGE,
                    border_radius=25
                )
            )
        return container_list

    row = ft.Row(controls=create_container(8), alignment=ft.MainAxisAlignment.CENTER)
    page.add(row)


ft.app(target=main)