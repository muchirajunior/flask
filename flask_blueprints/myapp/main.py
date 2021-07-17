from flask import Flask
from .site.routes import site
from .api.routes import api
from .myadmin.routes import myadmin


app=Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(site)
app.register_blueprint(myadmin)
