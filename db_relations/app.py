from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///one.db"
app.config['SQLALCHEMY_BINDS']={
    "two":"sqlite:///two.db",
    "three":"sqlite:///three.db"
}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db=SQLAlchemy(app)

class First(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)

    def __init__(self,name):
        self.name=name


class Second(db.Model):
    __bind_key__="two"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)

    def __init__(self,name):
        self.name=name


class Third(db.Model):
    __bind_key__="three"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)

    def __init__(self,name):
        self.name=name
        

@app.route("/")
def index():
    
    return "running!!!!!!!!!1"

@app.route("/one/<name>")
def one(name):
    db.session.add(First(name))
    db.session.commit()

    return "added to one succesfully"

@app.route("/two/<name>")
def two(name):
    db.session.add(Second(name))
    db.session.commit()

    return "added to two succesfully"

@app.route("/three/<name>")
def three(name):
    db.session.add(Third(name))
    db.session.commit()

    return "added to three succesfully"

if __name__=="__main__":
    app.run(debug=True)