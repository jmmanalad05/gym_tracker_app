from flask import Flask
from app.extensions.db import Database
import secrets

db = Database()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secrets.token_hex(32)

    # initialize DB
    db.connect()

    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    return app