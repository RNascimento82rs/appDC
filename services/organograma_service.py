from ..models.organograma import Organograma
from .. import db

def get_organograma(id):
    return Organograma.query.get(id)

def get_all_organogramas():
    return Organograma.query.all()

def add_organograma(municipio_id, nome, tipo_incidente, estrutura_json):
    db.session.add(Organograma(
        municipio_id=municipio_id,
        nome=nome,
        tipo_incidente=tipo_incidente,
        estrutura_json=estrutura_json
    ))
    db.session.commit()

def edit_organograma(id, nome, tipo_incidente, estrutura_json):
    org = Organograma.query.get(id)
    if org:
        org.nome = nome
        org.tipo_incidente = tipo_incidente
        org.estrutura_json = estrutura_json
        db.session.commit()

def delete_organograma(id):
    org = Organograma.query.get(id)
    if org:
        db.session.delete(org)
        db.session.commit()
