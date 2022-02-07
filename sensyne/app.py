from flasgger import Swagger
from flask import abort, current_app, Blueprint, Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from sensyne.db import db
from sensyne.api import bp
from sensyne.utils import init_db
from sensyne.config import DevConfig

def create_app(config_object=None):
    if config_object is None:
        config_object = DevConfig

    app = Flask('sensyne')
    app.config.from_object(config_object)
    swagger = Swagger(app)

    app.register_blueprint(bp, url_prefix='/v1')
    
    init_db(db, app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)