from flask import Flask
from .site.routes import site
from .api.routes import api


app=Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(site)
