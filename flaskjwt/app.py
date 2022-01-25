# type:ignore
from datetime import timedelta
from flask import Flask
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"]=timedelta(seconds=30)
jwt = JWTManager(app)


# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.post("/login")
def login():
    user=request.json
    print(user)
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username == "test" or password == "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=user)
    return jsonify(access_token=access_token)


# user a route with jwt_required, which will kick out requests
# without a valid JWT present.
@app.get("/user")
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user ), 200


if __name__ == "__main__":
    app.run(debug=True)