import flet as ft


def build_navbar(page_title: str, on_back=None):
    """Barra superior reutilizável."""
    back_btn = ft.IconButton(
        ft.Icons.ARROW_BACK,
        tooltip="Voltar",
        on_click=lambda e: on_back() if on_back else None
    ) if on_back else ft.Container(width=40)

    return ft.Row([
        back_btn,
        ft.Text(page_title, size=20, weight="bold"),
        ft.Container(expand=True)
    ], alignment=ft.MainAxisAlignment.START)
