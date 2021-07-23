from flask import Flask,jsonify,json
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///mydb.db"

db=SQLAlchemy(app)
ma=Marshmallow(app)

class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    password=db.Column(db.String)

    def __init__(self,name,password):
        self.name=name
        self.password=password


class UsersSchema(ma.Schema):
    class Meta:
        fields=('name','password')
userschema=UsersSchema()
usersschema=UsersSchema(many=True)

@app.route('/')
def index():

    return {"app":"running"}

@app.route('/alldata')
def alldata():
    users=Users.query.all()
    users=usersschema.dump(users)

    return jsonify(users)

@app.route('/add/<name>/<password>')
def add(name,password):
    db.session.add(Users(name,password))
    db.session.commit()

    return "<h1>added user successfully</h1>"

@app.route('/search/<name>/<password>')
def search(name,password):
    try:
        user=Users.query.filter_by(name=name,password=password).first()
        user=userschema.dump(user)

        return userschema.jsonify(user)

    except:
        return {"feedback":"error"}

@app.route('/searchlike/<name>')
def searchlike(name):
    users=Users.query.filter(Users.name.like(f'%{name}%')).all()
    users=usersschema.dump(users)

    return usersschema.jsonify(users)

if __name__=="__main__":
    app.run(debug=True)