#this is the wsgi file
#running the scaled web app in myapp folder
from myapp.main import app 

if __name__=="__main__":
    app.run(debug=True)