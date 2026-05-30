import flet as ft
from src.state import state
from src.api import get_movies, create_movie


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


def build_add_movie_view(on_back, on_success, page):
    """Formulário para adicionar filme."""

    title_input = ft.TextField(
        label="Título do Filme",
        hint_text="Ex: Titanic"
    )

    feedback = ft.Text("", color="red")

    def on_submit(e):
        title = title_input.value.strip()

        if not title:
            feedback.value = "Informe o título do filme!"
            feedback.color = "red"
            page.update()
            return

        try:
            create_movie(title)
            on_success()
        except Exception as err:
            feedback.value = f"Erro: {str(err)}"
            feedback.color = "red"
            page.update()

    return ft.Column([
        ft.Text("Novo Filme", size=25, weight="bold"),
        ft.Divider(),
        title_input,
        ft.Row(
            [
                ft.ElevatedButton("Voltar", on_click=lambda e: on_back()),
                ft.ElevatedButton("Cadastrar", on_click=on_submit),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        feedback
    ], spacing=15)