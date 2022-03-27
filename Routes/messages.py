from flask import Blueprint, render_template
from models.messages import messagess


contactperu = Blueprint("mensajes", __name__, url_prefix="/")

@contactperu.route("/messages",  methods=["GET", "POST"])
def nuevosmensajes():
    listamensajes = messagess.query.all()
    return render_template("messages.html", listamensajes=listamensajes)