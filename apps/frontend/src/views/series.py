import flet as ft
from src.state import state
from src.api import get_series


def build_series_view(on_series_click):
    """View que lista todas as séries."""
    list_items = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO)

    try:
        state.series = get_series()
    except Exception as e:
        return ft.Column([
            ft.Text("Séries", size=25, weight="bold"),
            ft.Text(f"Erro ao carregar: {str(e)}", color="red")
        ])

    if not state.series:
        list_items.controls.append(
            ft.Text("Nenhuma série cadastrada.", color="grey")
        )
    else:
        for serie in state.series:
            list_items.controls.append(
                ft.Container(
                    content=ft.ListTile(
                        title=ft.Text(serie.get("title", ""), weight="bold"),
                        leading=ft.Icon(ft.Icons.TV),
                        on_click=lambda e, s=serie: on_series_click(s)
                    ),
                    border=ft.Border.all(1, ft.Colors.OUTLINE_VARIANT),
                    border_radius=10
                )
            )

    return ft.Column([
        ft.Text("Séries", size=25, weight="bold"),
        ft.Divider(),
        list_items
    ], spacing=15)
