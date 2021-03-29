from flask import Flask,render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db=SQLAlchemy(app)




@app.route("/")
def index():
    if request.method=="POST":
        pass
    else:
        return render_template("index.html")


@app.route("/comments")
def comments():
    return render_template("comments.html")

@app.route("/blogs/<string:username>")
def blogs(username):
    return "HELLO BLOGGER %s" %username

if __name__=="__main__":
    app.run(debug=True,port=5000)
