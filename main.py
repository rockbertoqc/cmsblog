from flask import Flask, render_template
from sqlalchemy_utils import create_database, database_exists
from backend.config.settings import Settings, security, db, bc, ckeditor, login, uri
blog=Flask(__name__)

blog.config.from_object(Settings)
security.init_app(blog)
db.init_app(blog)
bc.init_app(blog)
ckeditor.init_app(blog)
login.init_app(blog)

login.login_view='acceso.login'
from backend.views.admin.acceso import acceso
from backend.config.setup import setup
from backend.views.admin.panel import cms
from backend.views.admin.category import categoria
from backend.views.admin.posts import articulos
from backend.views.blog.blog import blogview

blog.register_blueprint(cms)
blog.register_blueprint(acceso)
blog.register_blueprint(setup)
blog.register_blueprint(categoria)
blog.register_blueprint(articulos)
blog.register_blueprint(blogview)





@blog.teardown_appcontext
def cerrar_basededatos(exception=None):
    db.session.remove()






from backend.config.models import Users
@login.user_loader
def select_user(id):
    username=Users.query.get(id)
    if username:
        return username

with blog.app_context():
    if not database_exists(uri):
        create_database(uri)
    db.create_all()



