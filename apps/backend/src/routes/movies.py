from flask import Blueprint, jsonify, request
from src.schemas.movie_schema import MovieSchema
from src.models import Movie, db

movies_bp = Blueprint('movies', __name__)

@movies_bp.route('/', methods=['GET'])
def get_movies():
    """
    Lista todos os filmes
    ---
    tags:
      - Filmes
    responses:
      200:
        description: Lista de filmes
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              title:
                type: string
    """
    movies = Movie.query.all()
    result = [MovieSchema(**m.to_dict()).model_dump() for m in movies]
    return jsonify(result)

@movies_bp.route('/', methods=['POST'])
def create_movie():
    """
    Cria um novo filme
    ---
    tags:
      - Filmes
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - title
          properties:
            title:
              type: string
              example: "Interestelar"
    responses:
      201:
        description: Filme criado
    """
    data = request.get_json()
    new_movie = Movie(title=data['title'])
    db.session.add(new_movie)
    db.session.commit()
    return jsonify(MovieSchema(**new_movie.to_dict()).model_dump()), 201

@movies_bp.route('/<int:id>', methods=['PUT'])
def update_movie(id):
    """
    Atualiza um filme existente
    ---
    tags:
      - Filmes
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
    responses:
      200:
        description: Filme atualizado
    """
    movie = Movie.query.get_or_404(id)
    data = request.get_json()
    movie.title = data.get('title', movie.title)
    db.session.commit()
    return jsonify(MovieSchema(**movie.to_dict()).model_dump())

@movies_bp.route('/<int:id>', methods=['DELETE'])
def delete_movie(id):
    """
    Remove um filme
    ---
    tags:
      - Filmes
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Filme removido
    """
    movie = Movie.query.get_or_404(id)
    db.session.delete(movie)
    db.session.commit()
    return jsonify({"message": "Removido com sucesso"}), 200