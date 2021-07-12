from flask import Blueprint

api=Blueprint('api',__name__, url_prefix="/api")

@api.route("/")
def home():

    return {"state":"running"}

@api.route("/user/<id>")      
def user(id):

    return {"userId":id}
