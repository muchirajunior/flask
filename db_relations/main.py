from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///mydb.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
ma=Marshmallow(app)

class Doctor(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String, unique=True)
    place=db.Column(db.String)
    hospital=db.Column(db.String)
    patient=db.relationship('Patient',backref='doctor', lazy=True)

    def __init__(self,name,place,hospital):
        self.name=name
        self.place=place
        self.hospital=hospital

class Patient(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    place=db.Column(db.String)
    mydoctor=db.Column(db.String, db.ForeignKey('doctor.name'))

    def __init__(self,name,place,doctor):
        self.name=name
        self.place=place
        self.mydoctor=doctor

class MySchema(ma.Schema):
    class Meta:
        fields=('name','place','mydoctor')

myschemas=MySchema(many=True)
myschema=MySchema()

class DoctorSchema(ma.Schema):
    patient=ma.Nested(MySchema, many=True)
    class Meta:
        fields=('name','place','mydoctor','patient','hospital')

docschema=DoctorSchema()
docschemas=DoctorSchema(many=True)

@app.route('/')
def home():
    return {"state":"running"}

@app.route('/doctor')
def mydoctor():
    doc=Doctor.query.filter_by(name='junior').first()
    doc=docschema.dump(doc)

    return docschema.jsonify(doc)

@app.route('/doctors')
def mydocs():
    docs=Doctor.query.all()
    docs=docschemas.dump(docs)
   
    return docschemas.jsonify(docs)

@app.route('/patient')
def mypatient():
    pat=Patient.query.filter_by(name='muchira').first()
    pat=myschema.dump(pat)

    return myschema.jsonify(pat)


if __name__=="__main__":
    app.run(debug=True) 