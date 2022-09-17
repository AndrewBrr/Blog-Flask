##___________________________________________________________________________IMPORTS___________________________________________________________________________________________

from distutils.log import error
from sre_constants import SUCCESS
from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
##__________________________________________________________________________Autenticaciones____________________________________________________________________________________
auth = Blueprint("auth", __name__)

@auth.route("/portal")
def portal():
    return "inicio"

@auth.route("/login", methods=['GET', 'POST'])
def login():

    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()
    if user:
        if check_password_hash(user.password, password):
            flash("sesion iniciada", category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.portal'))
        else:
            flash('Contraseña incorrecta, por favor intentar de nuevo', category='error')
    else:
        flash('Usuario no registrado', category='error')

    return render_template("login.html")


@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():

    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        email_existe = User.query.filter_by(email=email).first() ## para crear un nuevo usuario hay que verificar primero que no exista tal usuario, con este codigo
        usuario_existe = User.query.filter_by(username=username).first()

        if email_existe:
            flash ('El correo ya ha sido utilizado', category = 'error')
        elif usuario_existe:
            flash ('El usuario ya se encuentra en uso', category = 'error')
        elif password1 != password2:
            flash ('Las contraseñas no son iguales')
        elif len(username) < 2:
            flash ('El usuario es demasiado corto', category = 'error')
        elif len(password1) < 6:
            flash('esta contraseña es demasiado corta')
        elif len(email) < 10:
            flash('correo invalido', category = 'error')
        else:
            nuevo_usuario = User(email=email, username=username, password=generate_password_hash(password1, method = 'sha256'))  ##estos son los parametros para crear un usuario valido y la forma de verificar si cumple los requisitos
                                                                                                                                 ##sha256 es un metodo basico de encriptacion
            db.session.add(nuevo_usuario) ## con esto se prepara para agregar el nuevo usuario registrado
            db.session.commit() ## y con esto se lo agregaa la base de datos una vez creado
            login_user(nuevo_usuario, remember=True)
            flash ('usuario creado')

            return redirect(url_for('views.portal'))
    
    
    return render_template("sign_up.html")


@auth.route("/logout", methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))