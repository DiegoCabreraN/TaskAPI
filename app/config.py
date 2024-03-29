from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=True)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sunshop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)