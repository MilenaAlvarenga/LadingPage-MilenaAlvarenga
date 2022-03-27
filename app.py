from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils.db import db
from Routes.home import home
from Routes.messages import contactperu

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)

# register blueprints
app.register_blueprint(home)
app.register_blueprint(contactperu)
