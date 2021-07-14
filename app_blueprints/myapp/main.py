from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from flask_login import UserMixin,LoginManager,login_required, login_user, current_user, logout_user

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///mydb.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SECRET_KEY"]="xyz123"

db=SQLAlchemy(app)

#declare and initialize login manager for the flask app
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view="site.login" #if user is not login redirect to login route

def authorization(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token=None

        if "auth" in request.headers:
            token=request.headers['auth']

            if token != app.config["SECRET_KEY"]:
                return {"feedback":"invalid token"}

        else:
             return {"feedback":"missing token"}

        return f(*args, **kwargs)

    return decorator


#create the decorator
@login_manager.user_loader
def load_user(user_id):
    return user_id
