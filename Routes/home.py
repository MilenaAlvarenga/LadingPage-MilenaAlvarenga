from flask import Blueprint, render_template, redirect, url_for
from models.messages import messagess
from forms.contactusform import contactme
from utils.db import db

home = Blueprint("home", __name__)

@home.route("/", methods=["GET", "POST"])
def mensajenuevo():
    form = contactme()
    if form.validate_on_submit():
            fullname = form.fullname.data
            email = form.email.data
            message = form.message.data
            newmessage = messagess(fullname, email, message)
            db.session.add(newmessage)
            db.session.commit()
    return render_template("home.html", form=form)

