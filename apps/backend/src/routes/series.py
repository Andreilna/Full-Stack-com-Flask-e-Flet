from flask import Blueprint, jsonify, request
from src.schemas.series_schema import SeriesSchema
from src.models import Series, db

series_bp = Blueprint('series', __name__)

@series_bp.route('/', methods=['GET'])
def get_series():
    """
    Lista todas as séries
    ---
    tags:
      - Séries
    """
    series = Series.query.all()
    result = [SeriesSchema(**s.to_dict()).model_dump() for s in series]
    return jsonify(result)

@series_bp.route('/', methods=['POST'])
def create_series():
    """ Cria uma nova série """
    data = request.get_json()
    new_series = Series(title=data['title'])
    db.session.add(new_series)
    db.session.commit()
    return jsonify(SeriesSchema(**new_series.to_dict()).model_dump()), 201

@series_bp.route('/<int:id>', methods=['PUT'])
def update_series(id):
    serie = Series.query.get_or_404(id)
    data = request.get_json()
    serie.title = data.get('title', serie.title)
    db.session.commit()
    return jsonify(SeriesSchema(**serie.to_dict()).model_dump())

@series_bp.route('/<int:id>', methods=['DELETE'])
def delete_series(id):
    serie = Series.query.get_or_404(id)
    db.session.delete(serie)
    db.session.commit()
    return jsonify({"message": "Série removida"}), 200