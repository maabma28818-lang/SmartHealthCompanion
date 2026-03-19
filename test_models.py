#!/usr/bin/env python3

import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# Create a simple test app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Now import and test models
with app.app_context():
    # Import models after app context is created
    from models import User, Doctor, Patient
    
    # Create tables
    db.create_all()
    
    print("Models imported and tables created successfully!")
    print("Available tables:", db.engine.table_names())