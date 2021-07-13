from  flask import Blueprint
from .model import Admins
from ..main import db

myadmin=Blueprint('myadmin',__name__,url_prefix="/myadmin")

@myadmin.route('/')
def index():

    return "<h1>THIS IS MYADMIN PAGE</h1>"

@myadmin.route('/adminadd/<name>')
def adminadd(name):
    db.session.add(Admins(name))
    db.session.commit()

    return "added admin "+name+" succesfully"