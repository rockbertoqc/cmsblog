from backend.config.settings import db, bc
from backend.config.models import Users
from flask import Blueprint, redirect, url_for

setup=Blueprint('setup', __name__)

@setup.route('/setup/new_admin')
def new_admin():
    password = '123456a'
    hash=bc.generate_password_hash(password).decode('utf-8')
    query=Users(nombre='Administrador', usuario='admin', clave=hash, correo='pedorro@gmail.com')
    db.session.add(query)
    db.session.commit()
    return redirect(url_for('acceso.login'))


    