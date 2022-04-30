from .bluprints import person_bp
from flask import redirect, url_for


def init_app(app):

    @app.route('/')
    def home():
        return redirect('/person')

    app.register_blueprint(person_bp, url_prefix='/person')
