from flask import Flask
from .extensions import ensure
from config import Config
from .blueprints.auth import auth_bp
from .blueprints.main import main_bp
from .fmdb.FMDB import *
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    blueprints = {
        "auth_bp": auth_bp,
        "main_bp": main_bp
    }

    ensure(app, "auth_bp", blueprints)
    ensure(app, "main_bp", blueprints)

    return app
