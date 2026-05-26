import flet as ft
from src.state import state
from src.api import get_actors


def build_actors_view(on_actor_click):
    """View que lista todos os atores."""
    list_items = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO)

    try:
        state.actors = get_actors()
    except Exception as e:
        return ft.Column([
            ft.Text("Atores", size=25, weight="bold"),
            ft.Text(f"Erro ao carregar: {str(e)}", color="red")
        ])

    if not state.actors:
        list_items.controls.append(
            ft.Text("Nenhum ator cadastrado.", color="grey")
        )
    else:
        for actor in state.actors:
            list_items.controls.append(
                ft.Container(
                    content=ft.ListTile(
                        title=ft.Text(actor.get("name", ""), weight="bold"),
                        leading=ft.Icon(ft.Icons.PERSON),
                        on_click=lambda e, a=actor: on_actor_click(a)
                    ),
                    border=ft.Border.all(1, ft.Colors.OUTLINE_VARIANT),
                    border_radius=10
                )
            )

    return ft.Column([
        ft.Text("Atores", size=25, weight="bold"),
        ft.Divider(),
        list_items
    ], spacing=15)
