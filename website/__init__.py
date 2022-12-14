##_____________________________________________________________________++IMPORTS++________________________________________________________________________________________________________
import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

##_____________________________________________________________________++FUNCIONES Y CLASES++____________________________________________________________________________________


db = SQLAlchemy()
DB_NAME = "database.db"

def crear_app():
    app = Flask(__name__) ## Esto es lo primero y principal que hacer al crear una app en Flask, app es el nombre de la aplicacion  mientras que name referencia al modulo con el cual se va a correr la aplicacion
    app.config['SECRET_KEY'] = "holaatodos"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' ##esto es para decirle a flask donde se encuentra ubicada la base de datos
    db.init_app(app) 

    from .views import views
    from .auth import auth 
 
    
    app.register_blueprint(views, url_prefix="/") 
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Post


    create_database(app)

    

    login_manager = LoginManager()
    login_manager.login_view = "auth.login" ## en caso de que alguien intente ingresar a una pagina o visualizarla sin estar logeado, se le redirigira a la vista de login
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    

    return app


def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("¡Base de datos creada!")
