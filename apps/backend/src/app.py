import os
from flask import Flask
from flasgger import Swagger
from dotenv import load_dotenv
from .database import db, migrate

# Importar as rotas (Blueprints)
from .routes.movies import movies_bp
from .routes.series import series_bp
from .routes.actors import actors_bp
from .routes.genres import genres_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Configuração do Banco via .env
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializar extensões
    db.init_app(app)
    migrate.init_app(app, db)
    Swagger(app)

    # Registrar os 4 Blueprints
    app.register_blueprint(movies_bp, url_prefix='/movies')
    app.register_blueprint(series_bp, url_prefix='/series')
    app.register_blueprint(actors_bp, url_prefix='/actors')
    app.register_blueprint(genres_bp, url_prefix='/genres')

    return app