from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint("views", __name__)

@views.route("/") ## Con esto aun si no escribimos una direccion de ruta, por defecto nos devolvera al portal o pagina de inicio
@views.route("/portal")
@login_required
def portal():
    return render_template("portal.html", name = "Andrew")
