SCALLING FLASK
----------------

flask app divison into smaller subapps

this helps to scale a flask application

myapp directory carries the whole app and consist a __init__ file to make the 
application a package

the main.py file contain the app or the setup/settings of both flask app and
 flask_sqlalchemy database object db

they are run on the __init__.py file and all blueprints are registered here

each Blueprint/subapp contains a __init__ file to make them a package easy to 
be imported for use

all the database classes are put in model.py files and are implement db
flask_sqlalchemy object imported from the main.py 

the model classes are imported to __init__ files to make sure that they are 
run whenever the app is run and for use in adding data to the database
