from .. import db

class Municipio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    organogramas = db.relationship('Organograma', backref='municipio', lazy=True)
