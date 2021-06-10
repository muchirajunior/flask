from flask_bcrypt import Bcrypt
from flask import Flask

app = Flask(__name__)
bcrypt = Bcrypt(app)

pw_hash = bcrypt.generate_password_hash('secret', 10)
isSamePassword = bcrypt.check_password_hash(pw_hash,"sercret")

print(pw_hash)
print(isSamePassword)