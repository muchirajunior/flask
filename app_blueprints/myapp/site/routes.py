from flask import Blueprint
from ..main import login_required, login_user, current_user, logout_user
from .models import User,db

site=Blueprint('site',__name__)

@site.route("/")
def index():

    return "<h1>THIS IS THE HOME PAGE</h1>"

@site.route('/register/<name>')
def register(name):
    db.session.add(User(name=name))
    db.session.commit()

    return  "added user "+name+" sucessfully"

@site.route('/login')
def login():
    user=User.query.filter_by(name="junior").first()
    login_user(user)

    return "<h1>LOGGED IN USER </h1>"


@site.route('/userpage')
@login_required
def user():
   
    return "<h1>THIS IS USER PAGE</h1>"

@site.route('/logout')
@login_required
def logout():
    

    return "<h1>LOGGED OUT USER </h1>"


