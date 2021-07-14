from flask import Blueprint
from ..main import authorization
api=Blueprint('api',__name__,url_prefix="/api")

@api.route("/")
def Index():

    return {"state":"runninng"}

@api.route("/protected")
@authorization
def protected():

    return {"feedback":"accessed!!!!!!"}
    
     