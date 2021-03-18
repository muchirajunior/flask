from flask import Flask,request,render_template,url_for,redirect, session
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False
db=SQLAlchemy(app)

app.secret_key="junior5678"
app.permanent_session_lifetime=timedelta(minutes=5)

class Users(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    username=db.Column(db.String(50))
    email=db.Column(db.String(100))

    def __init__(self,name,username,email):
        self.name=name
        self.username=username
        self.email=email
        
@app.route("/",methods=['POST','GET'])
def home():
    if request.method=="POST":
        session.permanent=True
        username=request.form['username']
        email=request.form['email']
        session['user']=username
        session['email']=email

        return redirect('admin')
    else:
        if 'user' in session:
            return redirect('admin')
        else:
            return render_template("login.html")

@app.route("/admin", methods=['POST','GET'])
def admin():
    if 'user' in session:
        data=Users.query.all()
        
        return render_template('index.html',data=data,user=session['user'],email=session['email'])
    else:
        return redirect('/')


@app.route("/logout")
def logout():
    session.pop('user',None)
    return redirect('/')

@app.route("/insert", methods=['POST','GET'])
def insert():
    if 'user' in session:
        if request.method=="POST":
            name=request.form['name']
            username=request.form['username']
            email=request.form['email']
        
            newuser=Users(name,username,email)
            db.session.add(newuser)
            db.session.commit()
            
            return redirect("/admin")

        else:
            return render_template('adduser.html')

    else:
        return redirect('/')

@app.route('/update')
def update():
    if 'user' in session:
        return render_template('/sample/update.html')

    else:
        return redirect('/')

@app.errorhandler(404)
def errorpage(error):

    return render_template('notfound.html')



if __name__=="__main__":
    app.run(debug=True)
