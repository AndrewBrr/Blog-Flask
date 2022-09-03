from enum import unique
from time import timezone
from . import db  ##el punto señala el paquete en el que nos encontramos ahora mismo, es decir, en website
from flask_login import UserMixin
from sql_alchemy.sql import func


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key= True) ## id va a ser la columna primaria para almacemar/buscar los usuarios que se registran en la db
    email = db.Column(db.String(150), unique = True) 
    username = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    date_creation = db.Column(db.Date(timezone=True), default=func.now())  