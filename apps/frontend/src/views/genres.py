import flet as ft
from src.state import state
from src.api import get_genres


def build_genres_view(on_genre_click):
    """View que lista todos os gêneros."""
    list_items = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO)

    try:
        state.genres = get_genres()
    except Exception as e:
        return ft.Column([
            ft.Text("Gêneros", size=25, weight="bold"),
            ft.Text(f"Erro ao carregar: {str(e)}", color="red")
        ])

    if not state.genres:
        list_items.controls.append(
            ft.Text("Nenhum gênero cadastrado.", color="grey")
        )
    else:
        for genre in state.genres:
            list_items.controls.append(
                ft.Container(
                    content=ft.ListTile(
                        title=ft.Text(genre.get("name", ""), weight="bold"),
                        leading=ft.Icon(ft.Icons.LABEL),
                        on_click=lambda e, g=genre: on_genre_click(g)
                    ),
                    border=ft.Border.all(1, ft.Colors.OUTLINE_VARIANT),
                    border_radius=10
                )
            )

    return ft.Column([
        ft.Text("Gêneros", size=25, weight="bold"),
        ft.Divider(),
        list_items
    ], spacing=15)
