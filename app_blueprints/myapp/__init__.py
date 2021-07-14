from .main import app,db

from .site.routes import site

app.register_blueprint(site)
