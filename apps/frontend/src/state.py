class AppState:
    def __init__(self) -> None:
        self.user_id = 1
        self.movies: list[dict] = []
        self.actors: list[dict] = []
        self.genres: list[dict] = []
        self.series: list[dict] = []
        self.current_movie: dict | None = None
        self.current_actor: dict | None = None
        self.current_genre: dict | None = None
        self.current_series: dict | None = None
        self.feedback_message = ""
        self.feedback_type = "success"  # "success" ou "error"

    def reset_movie_state(self) -> None:
        """Limpa o estado ao voltar para a lista de filmes."""
        self.current_movie = None
        self.feedback_message = ""
        self.feedback_type = "success"


state = AppState()
