from os import path
from flask import Flask, render_template
from inicial.inicial import inicial_blueprint
from Home.home import Home_blueprint
from Login.Login import login_blueprint
from database import db, login_manager


basedir = path.abspath(path.dirname(__file__))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + path.join(basedir, 'investimentos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'


db.init_app(app)
login_manager.init_app(app)

app.register_blueprint(inicial_blueprint)
app.register_blueprint(Home_blueprint)
app.register_blueprint(login_blueprint)
