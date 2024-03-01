from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Boolean, DateTime, JSON, func
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Todo(db.Model):
    id = db.Column(Integer, primary_key=True)
    recommendations = db.Column(db.JSON)