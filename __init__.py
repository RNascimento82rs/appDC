from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sua_chave_secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///municipios.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .routes.web_routes import web
    from .routes.api_routes import api
    app.register_blueprint(web)
    app.register_blueprint(api, url_prefix='/api')

    with app.app_context():
        db.create_all()

    return app
