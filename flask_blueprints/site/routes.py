from flask import Blueprint

site=Blueprint('site',__name__)

@site.route("/")
def index():

    return "<h1>THIS IS HOME PAGE </h1>"

@site.route("/user")
def user():

    return "user page 1"