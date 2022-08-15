from flask import Blueprint

views = Blueprint("views", __name__)

@views.route("/portal")
def portal():
    return "Portal"
