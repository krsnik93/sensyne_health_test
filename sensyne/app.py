from flasgger import Swagger
from flask import abort, current_app, Blueprint, Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from sensyne.db import db
from sensyne.api import bp
from sensyne.utils import init_db


def create_app(**config_kwargs):
    app = Flask('sensyne')

    for conf_key, conf_val in config_kwargs.items():
        app.config[conf_key] = conf_val

    swagger = Swagger(app)

    app.register_blueprint(bp, url_prefix='/v1')
    
    init_db(db, app)

    return app


if __name__ == "__main__":
    app = create_app({
        'SQLALCHEMY_DATABASE_URI': 'postgresql://postgres:postgres@db-sensyne/sensyne'
    })
    app.run(debug=True)