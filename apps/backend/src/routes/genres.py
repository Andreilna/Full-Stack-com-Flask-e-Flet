from flask import Blueprint, jsonify, request
from schemas.genre_schema import GenreSchema
from models import Genre, db

genres_bp = Blueprint('genres', __name__)

@genres_bp.route('/', methods=['GET'])
def get_genres():
    """
    Lista todos os gêneros
    ---
    tags:
      - Gêneros
    responses:
      200:
        description: Lista de gêneros
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
    """
    genres = Genre.query.all()
    result = [GenreSchema(**g.to_dict()).model_dump() for g in genres]
    return jsonify(result)


@genres_bp.route('/', methods=['POST'])
def create_genre():
    """
    Cria um novo gênero
    ---
    tags:
      - Gêneros
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - name
          properties:
            name:
              type: string
              example: "Ação"
    responses:
      201:
        description: Gênero criado
    """
    data = request.get_json()
    new_genre = Genre(name=data['name'])
    db.session.add(new_genre)
    db.session.commit()
    return jsonify(GenreSchema(**new_genre.to_dict()).model_dump()), 201


@genres_bp.route('/<int:id>', methods=['PUT'])
def update_genre(id):
    """
    Atualiza um gênero existente
    ---
    tags:
      - Gêneros
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
            name:
              type: string
    responses:
      200:
        description: Gênero atualizado
    """
    genre = Genre.query.get_or_404(id)
    data = request.get_json()
    genre.name = data.get('name', genre.name)
    db.session.commit()
    return jsonify(GenreSchema(**genre.to_dict()).model_dump())


@genres_bp.route('/<int:id>', methods=['DELETE'])
def delete_genre(id):
    """
    Remove um gênero
    ---
    tags:
      - Gêneros
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Gênero removido
    """
    genre = Genre.query.get_or_404(id)
    db.session.delete(genre)
    db.session.commit()
    return jsonify({"message": "Gênero removido"}), 200