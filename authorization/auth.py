#headers authorization token route decorator fuction
from functools import wraps
from flask import request
from tinydb import TinyDB,Query

db=TinyDB("data.json")
query=Query()

user=db.search(query.name=="junior")

print(user)

def authorization(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token=None

        if "authorization" in request.headers:
            token=request.headers['authorization']

            if token != user[0['key']]:
                print("invalid token")
                return {"feedback":"invalid token"}

        elif not token:
            print("missing token")
            return {"feedback":"missing token"}
        print("acces allowed")
        return f(*args, **kwargs)

    return decorator