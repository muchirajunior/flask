from ..main import db

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)

    def __init__(self,name):
        self.name=name

class SuperUser(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)

    def __init__(self,name):
        self.name=name