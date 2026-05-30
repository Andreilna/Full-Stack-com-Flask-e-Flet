import os
import httpx

API_URL = os.environ.get("API_URL", "http://localhost:5000")


def _request_json(method: str, path: str, json_data: dict | None = None) -> dict | list:
    """Função auxiliar para fazer requisições e tratar erros."""
    try:
        response = httpx.request(
            method=method,
            url=f"{API_URL}{path}",
            json=json_data,
            timeout=5.0,
            follow_redirects=True  # Segue redirects automaticamente
        )
        response.raise_for_status()
        return response.json()
    except Exception as exc:
        print(f"Erro na API ({path}): {exc}")
        raise RuntimeError(f"Erro ao conectar com o servidor: {exc}")


def get_movies() -> list[dict]:
    """Busca a lista de filmes do backend."""
    return _request_json("GET", "/movies/")


def create_movie(title: str) -> dict:
    """Cria um novo filme no backend."""
    return _request_json(
        "POST",
        "/movies/",
        json_data={"title": title}
    )


def update_movie(movie_id: int, title: str) -> dict:
    """Atualiza um filme no backend."""
    return _request_json(
        "PUT",
        f"/movies/{movie_id}",
        json_data={"title": title}
    )


def delete_movie(movie_id: int) -> dict:
    """Exclui um filme no backend."""
    return _request_json(
        "DELETE",
        f"/movies/{movie_id}"
    )


def get_actors() -> list[dict]:
    """Busca a lista de atores do backend."""
    return _request_json("GET", "/actors/")


def create_actor(name: str) -> dict:
    """Cria um novo ator no backend."""
    return _request_json(
        "POST",
        "/actors/",
        json_data={"name": name}
    )


def update_actor(actor_id: int, name: str) -> dict:
    """Atualiza um ator no backend."""
    return _request_json(
        "PUT",
        f"/actors/{actor_id}",
        json_data={"name": name}
    )


def delete_actor(actor_id: int) -> dict:
    """Exclui um ator no backend."""
    return _request_json(
        "DELETE",
        f"/actors/{actor_id}"
    )


def get_genres() -> list[dict]:
    """Busca a lista de gêneros do backend."""
    return _request_json("GET", "/genres/")


def create_genre(name: str) -> dict:
    """Cria um novo gênero no backend."""
    return _request_json(
        "POST",
        "/genres/",
        json_data={"name": name}
    )


def update_genre(genre_id: int, name: str) -> dict:
    """Atualiza um gênero no backend."""
    return _request_json(
        "PUT",
        f"/genres/{genre_id}",
        json_data={"name": name}
    )


def delete_genre(genre_id: int) -> dict:
    """Exclui um gênero no backend."""
    return _request_json(
        "DELETE",
        f"/genres/{genre_id}"
    )


def get_series() -> list[dict]:
    """Busca a lista de séries do backend."""
    return _request_json("GET", "/series/")


def create_series(title: str) -> dict:
    """Cria uma nova série no backend."""
    return _request_json(
        "POST",
        "/series/",
        json_data={"title": title}
    )


def update_series(series_id: int, title: str) -> dict:
    """Atualiza uma série no backend."""
    return _request_json(
        "PUT",
        f"/series/{series_id}",
        json_data={"title": title}
    )


def delete_series(series_id: int) -> dict:
    """Exclui uma série no backend."""
    return _request_json(
        "DELETE",
        f"/series/{series_id}"
    )