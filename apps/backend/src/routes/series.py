from flask import Blueprint, jsonify, request
from schemas.series_schema import SeriesSchema
from models import Series, db

series_bp = Blueprint('series', __name__)

@series_bp.route('/', methods=['GET'])
def get_series():
    """
    Lista todas as séries
    ---
    tags:
      - Séries
    responses:
      200:
        description: Lista de séries
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
    series = Series.query.all()
    result = [SeriesSchema(**s.to_dict()).model_dump() for s in series]
    return jsonify(result)


@series_bp.route('/', methods=['POST'])
def create_series():
    """
    Cria uma nova série
    ---
    tags:
      - Séries
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
              example: "Breaking Bad"
    responses:
      201:
        description: Série criada
    """
    data = request.get_json()
    new_series = Series(title=data['title'])
    db.session.add(new_series)
    db.session.commit()
    return jsonify(SeriesSchema(**new_series.to_dict()).model_dump()), 201


@series_bp.route('/<int:id>', methods=['PUT'])
def update_series(id):
    """
    Atualiza uma série existente
    ---
    tags:
      - Séries
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
        description: Série atualizada
    """
    serie = Series.query.get_or_404(id)
    data = request.get_json()
    serie.title = data.get('title', serie.title)
    db.session.commit()
    return jsonify(SeriesSchema(**serie.to_dict()).model_dump())


@series_bp.route('/<int:id>', methods=['DELETE'])
def delete_series(id):
    """
    Remove uma série
    ---
    tags:
      - Séries
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Série removida
    """
    serie = Series.query.get_or_404(id)
    db.session.delete(serie)
    db.session.commit()
    return jsonify({"message": "Série removida"}), 200