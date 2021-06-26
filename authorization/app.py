from flask import Flask,request
from functools import wraps
from auth import authorization

app=Flask(__name__)

app.config["SECRET_KEY"]="junior12"

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token=None

        if "auth" in request.headers:
            token=request.headers["auth"]

            if token != app.config["SECRET_KEY"]:
                return {"feedback":"invalid authorization token"}

        elif not token:
            return {"feedback":"missing authorizarion token"}

        return f(*args, **kwargs)

    return decorator


            

@app.route("/")
def index():

    return {"state":"running !!!!!!!"}

@app.route("/protected")
@token_required
def protected():
  
    return {"state":"accessed protected page"}

@app.route("/mypage")
@authorization
def mypage():

    return {"state":"accessed my authorized page "}

if __name__=="__main__":
    app.run(debug=True)