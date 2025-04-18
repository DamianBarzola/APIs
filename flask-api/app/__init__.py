from flask import Flask,render_template
from app.config import Config,DBConnector
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt


# load_dotenv()
app= Flask(__name__)
config = Config().dev_config
app.env=config.ENV
connector= DBConnector()

app.secret_key = os.environ.get("SECRET_KEY")
bcrypt = Bcrypt(app)

app.config["SQLALCHEMY_DATABASE_URI"]=connector.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = connector.SQLALCHEMY_TRACK_MODIFICATIONS

db = SQLAlchemy(app)

from app.routes import api
app.register_blueprint(api, url_prefix='/api')