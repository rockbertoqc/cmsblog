import os

uri=os.getenv('CMSBLOG')

class BasicSettings(object):
    DEBUG=True
    SECRET_KEY='123456A'

class Settings(BasicSettings):
    SQLALCHEMY_DATABASE_URI=uri
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    CKEDITOR_PKG_TYPE='standard'

from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
from flask_bcrypt import Bcrypt
bc=Bcrypt()
from flask_ckeditor import CKEditor
ckeditor=CKEditor()
from flask_login import LoginManager
login=LoginManager()
from flask_wtf.csrf import CSRFProtect
security=CSRFProtect()