import flet as ft
from src.state import state
from src.api import get_movies


def build_movies_view(on_movie_click):
    """View que lista todos os filmes."""
    list_items = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO)

    try:
        state.movies = get_movies()
    except Exception as e:
        return ft.Column([
            ft.Text("Catálogo de Filmes", size=25, weight="bold"),
            ft.Text(f"Erro ao carregar: {str(e)}", color="red")
        ])

    if not state.movies:
        list_items.controls.append(
            ft.Text("Nenhum filme cadastrado.", color="grey")
        )
    else:
        for movie in state.movies:
            list_items.controls.append(
                ft.Container(
                    content=ft.ListTile(
                        title=ft.Text(movie.get("title", ""), weight="bold"),
                        leading=ft.Icon(ft.Icons.MOVIE),
                        on_click=lambda e, m=movie: on_movie_click(m)
                    ),
                    border=ft.Border.all(1, ft.Colors.OUTLINE_VARIANT),
                    border_radius=10
                )
            )

    return ft.Column([
        ft.Text("Catálogo de Filmes", size=25, weight="bold"),
        ft.Divider(),
        list_items
    ], spacing=15)
