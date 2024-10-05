from flask_sqlalchemy import SQLAlchemy
from .fmdb.FMDB import *


def ensure(app, name, blueprints):
    if name in blueprints:
        app.register_blueprint(blueprints[name])
    else:
        raise ValueError(f"Blueprint '{name}' bulunamadı.")

def model():
    user_db = JSONDatabase('users')
    user_db.add_user('admin', 'pass')
    print(user_db.get_users())


model()