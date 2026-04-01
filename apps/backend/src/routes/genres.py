from flask import Blueprint, jsonify, request
from src.schemas.genre_schema import GenreSchema
from src.models import Genre, db

genres_bp = Blueprint('genres', __name__)

@genres_bp.route('/', methods=['GET'])
def get_genres():
    """
    Lista todos os gêneros
    ---
    tags:
      - Gêneros
    """
    genres = Genre.query.all()
    result = [GenreSchema(**g.to_dict()).model_dump() for g in genres]
    return jsonify(result)

@genres_bp.route('/', methods=['POST'])
def create_genre():
    data = request.get_json()
    new_genre = Genre(name=data['name'])
    db.session.add(new_genre)
    db.session.commit()
    return jsonify(GenreSchema(**new_genre.to_dict()).model_dump()), 201

@genres_bp.route('/<int:id>', methods=['PUT'])
def update_genre(id):
    genre = Genre.query.get_or_404(id)
    data = request.get_json()
    genre.name = data.get('name', genre.name)
    db.session.commit()
    return jsonify(GenreSchema(**genre.to_dict()).model_dump())

@genres_bp.route('/<int:id>', methods=['DELETE'])
def delete_genre(id):
    genre = Genre.query.get_or_404(id)
    db.session.delete(genre)
    db.session.commit()
    return jsonify({"message": "Gênero removido"}), 200