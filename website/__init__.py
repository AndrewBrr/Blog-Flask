##_____________________________________________________________________++IMPORTS++________________________________________________________________________________________________________
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

##_____________________________________________________________________++FUNCIONES Y CLASES++____________________________________________________________________________________

def crear_app():

    app = Flask(__name__) ## Esto es lo primero y principal que hacer al crear una app en Flask, app es el nombre de la aplicacion  mientras que name referencia al modulo con el cual se va a correr la aplicacion
    app.config['SECRET_KEY'] = "holaatodos"

    from .views import views
    from .auth import auth 

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app

