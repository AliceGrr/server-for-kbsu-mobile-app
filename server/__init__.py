# server.__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

create_db = True
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from server import models
from server import routes
