from . import configuration
from . import database
from . import views
from flask import Flask

app = Flask(__name__)

configuration.init_app(app)
database.init_app(app)
views.init_app(app)

app.run()
