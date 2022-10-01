from enum import unique
from time import timezone
from . import db  ##el punto señala el paquete en el que nos encontramos ahora mismo, es decir, en website
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key= True) ## id va a ser la columna primaria para almacemar/buscar los usuarios que se registran en la db
    email = db.Column(db.String(150), unique = True) 
    username = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    date_creation = db.Column(db.DateTime(timezone=True), default=func.now())  
    posts = db.relationship('Post', backref='user', passive_deletes=True) ##esto permite borrar todos los post que el usuario creo cuando el usuario es eliminado 

class Post(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    text = db.Column(db.Text, nullable=False)
    date_creation = db.Column(db.DateTime(timezone=True), default=func.now())  
    autor = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
