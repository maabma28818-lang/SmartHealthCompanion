import os
import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix


# Set up logging
logging.basicConfig(level=logging.DEBUG)


class Base(DeclarativeBase):
    pass


# Create SQLAlchemy instance
db = SQLAlchemy(model_class=Base)


def create_app():
    # Create the app
    app = Flask(__name__)
    app.secret_key = os.environ.get("SESSION_SECRET", os.urandom(24))
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

    # Configure the database
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL", "sqlite:///healthcare.db"
    )
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_recycle": 300,
        "pool_pre_ping": True,
    }
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize DB with app
    db.init_app(app)

    return app


# Create the app instance
app = create_app()


def create_tables():
    """Create database tables"""
    with app.app_context():
        import models  # Import models so SQLAlchemy registers them
        db.create_all()