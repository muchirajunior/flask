from .main import app,db
from .home import site
from .admin import myadmin

app.register_blueprint(site)
app.register_blueprint(myadmin)
