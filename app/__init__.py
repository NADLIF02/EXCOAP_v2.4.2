from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    from .auth.views import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .event_calendar.views import calendar as calendar_blueprint
    app.register_blueprint(calendar_blueprint, url_prefix='/calendar')

    return app
