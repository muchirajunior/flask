from flask import Blueprint, render_template

myadmin=Blueprint('myadmin',__name__,url_prefix='/myadmin',template_folder="templates/myadmin")

@myadmin.route('/')
def index():

    return "<h1>my admin home page </h1>"

@myadmin.route("/user")
def user():

    return render_template('adminuser.html')