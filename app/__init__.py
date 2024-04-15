from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialisation de l'extension de la base de données
db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)  # Charger la configuration depuis une classe de configuration

    # Initialisation des extensions
    db.init_app(app)

    # Importation des Blueprints
    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from app.event_calendar import calendar as calendar_blueprint
    app.register_blueprint(calendar_blueprint)

    # Vous pouvez ajouter ici d'autres initialisations ou configurations d'extensions

    return app
