from flask import Flask,request,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_admin import Admin 
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin,LoginManager,login_required, login_user, current_user, logout_user
from datetime import timedelta


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///mydb.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SECRET_KEY"]="fgy8980okmn"

db=SQLAlchemy(app)
bcrypt=Bcrypt(app)

app.permanent_session_lifetime=timedelta(minutes=5) #user session lifetime

#declare and initialize login manager for the flask app
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view="login" #if user is not login redirect to login route

class  Users(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    username=db.Column(db.String,unique=True)
    email=db.Column(db.String)
    password=db.Column(db.String)
    
    def __init__(self,name,username,email,password):
        self.name=name
        self.username=username
        self.email=email
        self.password=password

class Admins(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    username=db.Column(db.String,unique=True)
    email=db.Column(db.String)

#setup the flask admin page
admin=Admin(app)
admin.add_view( ModelView(Users, db.session))
admin.add_view( ModelView(Admins, db.session))

#create the decorator
@login_manager.user_loader
def load_user(user_id):
    return Users.query.filter_by(id=user_id).first()

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/login", methods=['POST','GET'])
def login():

    if request.method=="POST":
        uname=request.form['username']
        password=request.form['password']

        if Users.query.filter_by(username=uname).first():
            user=Users.query.filter_by(username=uname).first()

            if bcrypt.check_password_hash(user.password, password): #check password
                login_user(user) #user data in the session
                return redirect('/user')

            else:
                return render_template("login.html", feedback="invalid  password ")
        else:
           return render_template("login.html", feedback="invalid  username ")

    return render_template("login.html")

@app.route("/register", methods=["POST","GET"])
def register():
    if request.method=="POST":
        name=request.form['name']
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']

        password=bcrypt.generate_password_hash(password,10)
        
        db.session.add(Users(name,username,email,password))
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")

@app.route("/user")
@login_required
def userpage():


    return render_template("user.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()

    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)