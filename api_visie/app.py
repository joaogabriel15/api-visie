from . import commands
from . import configuration
from . import database
from . import routes
from flask import Flask


def create_app():
    app = Flask(__name__)
    configuration.init_app(app)
    database.init_app(app)
    routes.init_app(app)
    commands.init_app(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
