import flet as ft
from src.state import state
from src.api import create_movie


def build_add_movie_view(on_back, on_success, page):
    """View com formulário para adicionar novo filme."""
    title_input = ft.TextField(
        label="Título do Filme",
        hint_text="Ex: Interestelar",
    )
    feedback = ft.Text("", color="red")

    def on_submit(e):
        title = title_input.value.strip()
        if not title:
            feedback.value = "Informe o título do filme!"
            feedback.color = "red"
        else:
            try:
                create_movie(title)
                feedback.value = "✓ Filme cadastrado com sucesso!"
                feedback.color = "green"
                title_input.value = ""
                page.update()
                on_success()
            except Exception as err:
                feedback.value = f"✗ Erro: {str(err)}"
                feedback.color = "red"
                page.update()

    submit_btn = ft.ElevatedButton("Cadastrar", on_click=on_submit)
    back_btn = ft.TextButton("← Voltar", on_click=lambda e: on_back())

    view_content = ft.Column([
        ft.Row([
            ft.Text("Novo Filme", size=25, weight="bold"),
            ft.Container(expand=True),
            back_btn
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Divider(),
        ft.Text("Preencha as informações abaixo:"),
        title_input,
        ft.Row([submit_btn], alignment=ft.MainAxisAlignment.CENTER),
        feedback
    ], spacing=15)

    return view_content
