from flask import Flask
from instance.config_dev import Config
from flask import jsonify
from pymongo import MongoClient
from .routes.activity import user_activity_bp
from .db import get_database


def create_app():
    app = Flask("Senseii", instance_relative_config=True)
    app.debug = True
    db = get_database

    # Below is a sample route to test if the flask server is working.
    @app.route("/hello")
    def hello():
        return jsonify("boobies")

    # register the blueprints to the server.
    app.register_blueprint(user_activity_bp)
    return app
