from ..models.municipio import Municipio
from .. import db

def get_municipios(per_page=10, offset=0):
    return Municipio.query.limit(per_page).offset(offset).all(), Municipio.query.count()

def add_municipio(nome, latitude, longitude):
    db.session.add(Municipio(nome=nome, latitude=latitude, longitude=longitude))
    db.session.commit()

def delete_municipio(id):
    municipio = Municipio.query.get(id)
    if municipio:
        db.session.delete(municipio)
        db.session.commit()
