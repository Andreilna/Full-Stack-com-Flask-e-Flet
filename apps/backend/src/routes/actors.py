from flask import Blueprint, jsonify, request
from src.schemas.actor_schema import ActorSchema
from src.models import Actor, db

actors_bp = Blueprint('actors', __name__)

@actors_bp.route('/', methods=['GET'])
def get_actors():
    """
    Lista todos os atores
    ---
    tags:
      - Atores
    """
    actors = Actor.query.all()
    result = [ActorSchema(**a.to_dict()).model_dump() for a in actors]
    return jsonify(result)

@actors_bp.route('/', methods=['POST'])
def create_actor():
    data = request.get_json()
    new_actor = Actor(name=data['name'])
    db.session.add(new_actor)
    db.session.commit()
    return jsonify(ActorSchema(**new_actor.to_dict()).model_dump()), 201

@actors_bp.route('/<int:id>', methods=['PUT'])
def update_actor(id):
    actor = Actor.query.get_or_404(id)
    data = request.get_json()
    actor.name = data.get('name', actor.name)
    db.session.commit()
    return jsonify(ActorSchema(**actor.to_dict()).model_dump())

@actors_bp.route('/<int:id>', methods=['DELETE'])
def delete_actor(id):
    actor = Actor.query.get_or_404(id)
    db.session.delete(actor)
    db.session.commit()
    return jsonify({"message": "Ator removido"}), 200