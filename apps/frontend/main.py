import flet as ft
from src.state import state
from src.api import (
    get_movies,
    create_movie,
    update_movie,
    delete_movie,
    get_actors,
    create_actor,
    update_actor,
    delete_actor,
    get_genres,
    create_genre,
    update_genre,
    delete_genre,
    get_series,
    create_series,
    update_series,
    delete_series,
)
from src.views.actors import build_actors_view
from src.views.genres import build_genres_view
from src.views.series import build_series_view
from src.views.movies import (
    build_movies_view,
    build_add_movie_view
)

def main(page: ft.Page):
    page.title = "Catálogo de Filmes"

    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLACK

    page.window_width = 600
    page.window_height = 800
    page.window.full_screen = True
    
    def render(view_content: ft.Control):
        """Limpa a tela e renderiza novo conteúdo."""
        page.clean()
        page.add(view_content)
        page.update()

    def build_navigation():
        return ft.Row([
            ft.ElevatedButton("Filmes", on_click=lambda e: show_movies()),
            ft.ElevatedButton("Atores", on_click=lambda e: show_actors()),
            ft.ElevatedButton("Gêneros", on_click=lambda e: show_genres()),
            ft.ElevatedButton("Séries", on_click=lambda e: show_series())
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=6)

    def build_route_toolbar(on_get, on_post, on_put, on_delete, put_disabled=False, delete_disabled=False):
        return ft.Row([
            ft.ElevatedButton("GET", on_click=on_get),
            ft.ElevatedButton("POST", on_click=on_post),
            ft.ElevatedButton("PUT", on_click=on_put, disabled=put_disabled),
            ft.ElevatedButton("DELETE", on_click=on_delete, disabled=delete_disabled)
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=8)

    def show_movies():
        """Exibe lista de filmes."""
        state.current_movie = None

        def on_movie_click(movie):
            show_movie_detail(movie)

        view = build_movies_view(on_movie_click=on_movie_click)
        toolbar = build_route_toolbar(
            on_get=lambda e: show_movies(),
            on_post=lambda e: show_add_movie(),
            on_put=lambda e: show_update_movie(state.current_movie) if state.current_movie else None,
            on_delete=lambda e: delete_movie_action(state.current_movie['id']) if state.current_movie else None,
            put_disabled=True,
            delete_disabled=True
        )

        header = ft.Row([
            ft.Text("Catálogo", size=28, weight="bold"),
            ft.Container(expand=True),
        ])

        content = ft.Column([ft.Text("Catálogo", size=28, weight="bold"), ft.Divider(), toolbar, view], spacing=10)
        render(ft.Column([build_navigation(), content, ft.Container(expand=True)], scroll=ft.ScrollMode.AUTO))

    def show_movie_detail(movie):
        """Exibe detalhes de um filme."""
        state.current_movie = movie

        toolbar = build_route_toolbar(
            on_get=lambda e: show_movies(),
            on_post=lambda e: show_add_movie(),
            on_put=lambda e: show_update_movie(movie),
            on_delete=lambda e: delete_movie_action(movie['id']),
            put_disabled=False,
            delete_disabled=False
        )

        back_btn = ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: show_movies())
        title = ft.Text(movie.get("title", ""), size=24, weight="bold")
        movie_id = ft.Text(f"ID: {movie.get('id', '?')}", size=14, color="grey")

        content = ft.Column([
            toolbar,
            ft.Row([back_btn, ft.Container(expand=True)]),
            title,
            movie_id,
            ft.Divider(),
            ft.Text("Detalhes", size=16, weight="bold"),
            ft.Text("Um filme do catálogo.")
        ], spacing=15)

        render(ft.Column([build_navigation(), content, ft.Container(expand=True)], scroll=ft.ScrollMode.AUTO))

    def show_actors():
        """Exibe lista de atores."""
        state.current_actor = None

        def on_actor_click(actor):
            show_actor_detail(actor)

        view = build_actors_view(on_actor_click=on_actor_click)
        toolbar = build_route_toolbar(
            on_get=lambda e: show_actors(),
            on_post=lambda e: show_add_actor(),
            on_put=lambda e: show_update_actor(state.current_actor) if state.current_actor else None,
            on_delete=lambda e: delete_actor_action(state.current_actor['id']) if state.current_actor else None,
            put_disabled=True,
            delete_disabled=True
        )

        content = ft.Column([
            ft.Text("Atores", size=28, weight="bold"),
            ft.Divider(),
            toolbar,
            view
        ], spacing=10)
        render(ft.Column([build_navigation(), content, ft.Container(expand=True)], scroll=ft.ScrollMode.AUTO))

    def show_actor_detail(actor):
        """Exibe detalhes de um ator."""
        state.current_actor = actor

        toolbar = build_route_toolbar(
            on_get=lambda e: show_actors(),
            on_post=lambda e: show_add_actor(),
            on_put=lambda e: show_update_actor(actor),
            on_delete=lambda e: delete_actor_action(actor['id']),
            put_disabled=False,
            delete_disabled=False
        )

        back_btn = ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: show_actors())
        title = ft.Text(actor.get("name", ""), size=24, weight="bold")

        content = ft.Column([
            toolbar,
            ft.Row([back_btn, ft.Container(expand=True)]),
            title,
            ft.Divider(),
            ft.Text("Detalhes do ator."),
            ft.Text(f"ID: {actor.get('id', '?')}", size=14, color="grey")
        ], spacing=15)

        render(ft.Column([build_navigation(), content, ft.Container(expand=True)], scroll=ft.ScrollMode.AUTO))

    def show_add_actor():
        name_input = ft.TextField(label="Nome do Ator", hint_text="Ex: Leonardo DiCaprio")
        feedback = ft.Text("", color="red")

        def on_submit(e):
            name = name_input.value.strip()
            if not name:
                feedback.value = "Informe o nome do ator!"
                feedback.color = "red"
            else:
                try:
                    create_actor(name)
                    show_actors()
                except Exception as err:
                    feedback.value = f"✗ Erro: {str(err)}"
                    feedback.color = "red"
                    page.update()

        content = ft.Column([
            ft.Text("Novo Ator", size=25, weight="bold"),
            ft.Divider(),
            name_input,
            ft.Row([ft.ElevatedButton("Cadastrar", on_click=on_submit)], alignment=ft.MainAxisAlignment.CENTER),
            feedback
        ], spacing=15)

        render(ft.Column([build_navigation(), content, ft.Container(expand=True)], scroll=ft.ScrollMode.AUTO))

    def show_update_actor(actor):
        if not actor:
            show_actors()
            return

        name_input = ft.TextField(label="Nome do Ator", value=actor.get("name", ""))
        feedback = ft.Text("", color="red")

        def on_submit(e):
            name = name_input.value.strip()
            if not name:
                feedback.value = "Informe o nome do ator!"
                feedback.color = "red"
            else:
                try:
                    update_actor(actor['id'], name)
                    show_actors()
                except Exception as err:
                    feedback.value = f"✗ Erro: {str(err)}"
                    feedback.color = "red"
                    page.update()

        content = ft.Column([
            ft.Text("Editar Ator", size=25, weight="bold"),
            ft.Divider(),
            name_input,
            ft.Row([ft.ElevatedButton("Salvar", on_click=on_submit)], alignment=ft.MainAxisAlignment.CENTER),
            feedback
        ], spacing=15)

        render(ft.Column([build_navigation(), content, ft.Container(expand=True)], scroll=ft.ScrollMode.AUTO))

    def delete_actor_action(actor_id):
        if not actor_id:
            show_actors()
            return
        try:
            delete_actor(actor_id)
            show_actors()
        except Exception as err:
            render(ft.Column([
                build_navigation(),
                ft.Text(f"Erro ao excluir ator: {str(err)}", color="red")
            ], scroll=ft.ScrollMode.AUTO))

    def show_genres():
        """Exibe lista de gêneros."""
        state.current_genre = None

        def on_genre_click(genre):
            show_genre_detail(genre)

        view = build_genres_view(on_genre_click=on_genre_click)
        toolbar = build_route_toolbar(
            on_get=lambda e: show_genres(),
            on_post=lambda e: show_add_genre(),
            on_put=lambda e: show_update_genre(state.current_genre) if state.current_genre else None,
            on_delete=lambda e: delete_genre_action(state.current_genre['id']) if state.current_genre else None,
            put_disabled=True,
            delete_disabled=True
        )

        content = ft.Column([
            ft.Text("Gêneros", size=28, weight="bold"),
            ft.Divider(),
            toolbar,
            view
        ], spacing=10)
        render(ft.Column([build_navigation(), content, ft.Container(expand=True)], scroll=ft.ScrollMode.AUTO))

    def show_genre_detail(genre):
        """Exibe detalhes de um gênero."""
        state.current_genre = genre

        toolbar = build_route_toolbar(
            on_get=lambda e: show_genres(),
            on_post=lambda e: show_add_genre(),
            on_put=lambda e: show_update_genre(genre),
            on_delete=lambda e: delete_genre_action(genre['id']),
            put_disabled=False,
            delete_disabled=False
        )

        back_btn = ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: show_genres())
        title = ft.Text(genre.get("name", ""), size=24, weight="bold")

        content = ft.Column([
            toolbar,
            ft.Row([back_btn, ft.Container(expand=True)]),
            title,
            ft.Divider(),
            ft.Text("Detalhes do gênero."),
            ft.Text(f"ID: {genre.get('id', '?')}", size=14, color="grey")
        ], spacing=15)

        render(ft.Column([build_navigation(), content, ft.Container(expand=True)], scroll=ft.ScrollMode.AUTO))

    def show_add_genre():
        name_input = ft.TextField(label="Nome do Gênero", hint_text="Ex: Ação")
        feedback = ft.Text("", color="red")

        def on_submit(e):
            name = name_input.value.strip()
            if not name:
                feedback.value = "Informe o nome do gênero!"
                feedback.color = "red"
            else:
                try:
                    create_genre(name)
                    show_genres()
                except Exception as err:
                    feedback.value = f"✗ Erro: {str(err)}"
                    feedback.color = "red"
                    page.update()

        content = ft.Column([
            ft.Text("Novo Gênero", size=25, weight="bold"),
            ft.Divider(),
            name_input,
            ft.Row([ft.ElevatedButton("Cadastrar", on_click=on_submit)], alignment=ft.MainAxisAlignment.CENTER),
            feedback
        ], spacing=15)

        render(ft.Column([build_navigation(), content, ft.Container(expand=True)], scroll=ft.ScrollMode.AUTO))

    def show_update_genre(genre):
        if not genre:
            show_genres()
            return

        name_input = ft.TextField(label="Nome do Gênero", value=genre.get("name", ""))
        feedback = ft.Text("", color="red")

        def on_submit(e):
            name = name_input.value.strip()
            if not name:
                feedback.value = "Informe o nome do gênero!"
                feedback.color = "red"
            else:
                try:
                    update_genre(genre['id'], name)
                    show_genres()
                except Exception as err:
                    feedback.value = f"✗ Erro: {str(err)}"
                    feedback.color = "red"
                    page.update()

        content = ft.Column([
            ft.Text("Editar Gênero", size=25, weight="bold"),
            ft.Divider(),
            name_input,
            ft.Row([ft.ElevatedButton("Salvar", on_click=on_submit)], alignment=ft.MainAxisAlignment.CENTER),
            feedback
        ], spacing=15)

        render(ft.Column([build_navigation(), content, ft.Container(expand=True)], scroll=ft.ScrollMode.AUTO))

    def delete_genre_action(genre_id):
        if not genre_id:
            show_genres()
            return
        try:
            delete_genre(genre_id)
            show_genres()
        except Exception as err:
            render(ft.Column([
                build_navigation(),
                ft.Text(f"Erro ao excluir gênero: {str(err)}", color="red")
            ], scroll=ft.ScrollMode.AUTO))

    def show_series():
        """Exibe lista de séries."""
        state.current_series = None

        def on_series_click(serie):
            show_series_detail(serie)

        view = build_series_view(on_series_click=on_series_click)
        toolbar = build_route_toolbar(
            on_get=lambda e: show_series(),
            on_post=lambda e: show_add_series(),
            on_put=lambda e: show_update_series(state.current_series) if state.current_series else None,
            on_delete=lambda e: delete_series_action(state.current_series['id']) if state.current_series else None,
            put_disabled=True,
            delete_disabled=True
        )

        content = ft.Column([
            ft.Text("Séries", size=28, weight="bold"),
            ft.Divider(),
            toolbar,
            view
        ], spacing=10)
        render(ft.Column([build_navigation(), content, ft.Container(expand=True)], scroll=ft.ScrollMode.AUTO))

    def show_series_detail(serie):
        """Exibe detalhes de uma série."""
        state.current_series = serie

        toolbar = build_route_toolbar(
            on_get=lambda e: show_series(),
            on_post=lambda e: show_add_series(),
            on_put=lambda e: show_update_series(serie),
            on_delete=lambda e: delete_series_action(serie['id']),
            put_disabled=False,
            delete_disabled=False
        )

        back_btn = ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: show_series())
        title = ft.Text(serie.get("title", ""), size=24, weight="bold")

        content = ft.Column([
            toolbar,
            ft.Row([back_btn, ft.Container(expand=True)]),
            title,
            ft.Divider(),
            ft.Text("Detalhes da série."),
            ft.Text(f"ID: {serie.get('id', '?')}", size=14, color="grey")
        ], spacing=15)

        render(ft.Column([build_navigation(), content, ft.Container(expand=True)], scroll=ft.ScrollMode.AUTO))

    def show_add_series():
        title_input = ft.TextField(label="Título da Série", hint_text="Ex: Stranger Things")
        feedback = ft.Text("", color="red")

        def on_submit(e):
            title = title_input.value.strip()
            if not title:
                feedback.value = "Informe o título da série!"
                feedback.color = "red"
            else:
                try:
                    create_series(title)
                    show_series()
                except Exception as err:
                    feedback.value = f"✗ Erro: {str(err)}"
                    feedback.color = "red"
                    page.update()

        content = ft.Column([
            ft.Text("Nova Série", size=25, weight="bold"),
            ft.Divider(),
            title_input,
            ft.Row([ft.ElevatedButton("Cadastrar", on_click=on_submit)], alignment=ft.MainAxisAlignment.CENTER),
            feedback
        ], spacing=15)

        render(ft.Column([build_navigation(), content, ft.Container(expand=True)], scroll=ft.ScrollMode.AUTO))

    def show_update_series(serie):
        if not serie:
            show_series()
            return

        title_input = ft.TextField(label="Título da Série", value=serie.get("title", ""))
        feedback = ft.Text("", color="red")

        def on_submit(e):
            title = title_input.value.strip()
            if not title:
                feedback.value = "Informe o título da série!"
                feedback.color = "red"
            else:
                try:
                    update_series(serie['id'], title)
                    show_series()
                except Exception as err:
                    feedback.value = f"✗ Erro: {str(err)}"
                    feedback.color = "red"
                    page.update()

        content = ft.Column([
            ft.Text("Editar Série", size=25, weight="bold"),
            ft.Divider(),
            title_input,
            ft.Row([ft.ElevatedButton("Salvar", on_click=on_submit)], alignment=ft.MainAxisAlignment.CENTER),
            feedback
        ], spacing=15)

        render(ft.Column([build_navigation(), content, ft.Container(expand=True)], scroll=ft.ScrollMode.AUTO))

    def delete_series_action(series_id):
        if not series_id:
            show_series()
            return
        try:
            delete_series(series_id)
            show_series()
        except Exception as err:
            render(ft.Column([
                build_navigation(),
                ft.Text(f"Erro ao excluir série: {str(err)}", color="red")
            ], scroll=ft.ScrollMode.AUTO))

    def show_add_movie():
        """Exibe formulário para adicionar filme."""
        view_content = build_add_movie_view(
            on_back=show_movies,
            on_success=show_movies,
            page=page
        )
        render(ft.Column([build_navigation(), view_content, ft.Container(expand=True)], scroll=ft.ScrollMode.AUTO))

    def show_update_movie(movie):
        if not movie:
            show_movies()
            return

        title_input = ft.TextField(label="Título do Filme", value=movie.get("title", ""))
        feedback = ft.Text("", color="red")

        def on_submit(e):
            title = title_input.value.strip()
            if not title:
                feedback.value = "Informe o título do filme!"
                feedback.color = "red"
            else:
                try:
                    update_movie(movie['id'], title)
                    show_movies()
                except Exception as err:
                    feedback.value = f"✗ Erro: {str(err)}"
                    feedback.color = "red"
                    page.update()

        content = ft.Column([
            ft.Text("Editar Filme", size=25, weight="bold"),
            ft.Divider(),
            title_input,
            ft.Row([ft.ElevatedButton("Salvar", on_click=on_submit)], alignment=ft.MainAxisAlignment.CENTER),
            feedback
        ], spacing=15)

        render(ft.Column([build_navigation(), content, ft.Container(expand=True)], scroll=ft.ScrollMode.AUTO))

    def delete_movie_action(movie_id):
        if not movie_id:
            show_movies()
            return
        try:
            delete_movie(movie_id)
            show_movies()
        except Exception as err:
            render(ft.Column([
                build_navigation(),
                ft.Text(f"Erro ao excluir filme: {str(err)}", color="red")
            ], scroll=ft.ScrollMode.AUTO))

    # --- Inicialização ---
    show_movies()


if __name__ == "__main__":
    ft.run(main)
