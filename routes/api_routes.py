from flask import Blueprint, jsonify
from ..services.municipio_service import get_municipios
from ..services.organograma_service import get_all_organogramas

api = Blueprint('api', __name__)

@api.route('/municipios')
def api_municipios():
    municipios, _ = get_municipios()
    return jsonify([
        {'id': m.id, 'nome': m.nome, 'latitude': m.latitude, 'longitude': m.longitude}
        for m in municipios
    ])

@api.route('/organogramas')
def api_organogramas():
    organogramas = get_all_organogramas()
    return jsonify([
        {'id': o.id, 'municipio_id': o.municipio_id, 'nome': o.nome, 'estrutura_json': o.estrutura_json}
        for o in organogramas
    ])
