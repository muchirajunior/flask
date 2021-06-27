flask-login and flask-admin
----------------------------

app registers users and hashes passwords using flask-bcrypt 

The app uses flask-login library to login users
it store user data  in a 5 minutes session

app also manages data using flask admin

there's user page that is protected for only logged in user 
using the flas_login @login_required decorator

there's a logout route that uses flask-login too 