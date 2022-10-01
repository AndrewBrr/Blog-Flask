from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Post
from . import db

views = Blueprint("views", __name__)

@views.route("/") ## Con esto aun si no escribimos una direccion de ruta, por defecto nos devolvera al portal o pagina de inicio
@views.route("/portal")
@login_required
def portal():
    return render_template("portal.html", user=current_user.username)

@views.route("/post", methods=['GET','POST'])
@login_required
def post():
    if request.method=='POST':
        text = request.form.get('text')

        if not text:
            flash('El post no puede estar vacio', category='error')
        else:
            post = Post(text=text, autor=current_user.id)
            db.session.add(post)  ##esto agregara el post creado con el id de usuario a la sesion de ese usuario
            db.session.commit()  ## y esto es para guardarlo en base de datos
            flash('post creado', category='success')


    return render_template('crear_post.html', user=current_user)