from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from ..model import Junior
from .model import User,SuperUser
from ..main import db
site=Blueprint('site',__name__)


@site.route("/")
def index():

    return "<h1> THIS IS THE HOME PAGE</h1>"

@site.route('/add/<name>')
def add(name):
    db.session.add(User(name))
    db.session.commit()

    return "added user : "+name

@site.route('/addjunior/<name>')
def addjunior(name):
    db.session.add(Junior(name))
    db.session.commit()

    return "added to junior user "+name

@site.route('/adduser/<name>')
def adduser(name):
    db.session.add(SuperUser(name))
    db.session.commit()

    return "added super user "+name+" successfully"