from .main import app,db

from .site.routes import site
from .api.routes import api

app.register_blueprint(site)
app.register_blueprint(api)