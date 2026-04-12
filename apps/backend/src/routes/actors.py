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
    responses:
      200:
        description: Lista de atores
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
    actors = Actor.query.all()
    result = [ActorSchema(**a.to_dict()).model_dump() for a in actors]
    return jsonify(result)


@actors_bp.route('/', methods=['POST'])
def create_actor():
    """
    Cria um novo ator
    ---
    tags:
      - Atores
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
              example: "Leonardo DiCaprio"
    responses:
      201:
        description: Ator criado
    """
    data = request.get_json()
    new_actor = Actor(name=data['name'])
    db.session.add(new_actor)
    db.session.commit()
    return jsonify(ActorSchema(**new_actor.to_dict()).model_dump()), 201


@actors_bp.route('/<int:id>', methods=['PUT'])
def update_actor(id):
    """
    Atualiza um ator existente
    ---
    tags:
      - Atores
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
        description: Ator atualizado
    """
    actor = Actor.query.get_or_404(id)
    data = request.get_json()
    actor.name = data.get('name', actor.name)
    db.session.commit()
    return jsonify(ActorSchema(**actor.to_dict()).model_dump())


@actors_bp.route('/<int:id>', methods=['DELETE'])
def delete_actor(id):
    """
    Remove um ator
    ---
    tags:
      - Atores
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Ator removido
    """
    actor = Actor.query.get_or_404(id)
    db.session.delete(actor)
    db.session.commit()
    return jsonify({"message": "Ator removido"}), 200
