from flask import Blueprint, redirect, render_template, url_for, request
from backend.config.settings import db, bc 
from backend.config.models import Users, Categorias, Posts
from flask_login import login_user, logout_user, current_user, login_required
from backend.config.forms import Login

acceso=Blueprint('acceso', __name__)

@acceso.route('/admin/login', methods=['GET', 'POST'])
def login():
    form=Login()
    if form.validate_on_submit():
        obtener_usuario=Users.query.filter_by(usuario=form.username.data).first()
        if obtener_usuario and bc.check_password_hash(obtener_usuario.clave, form.password.data):
            login_user(obtener_usuario)
            validando_status=Users.query.get(current_user.id) #Esto actualiza datos, el status de 0 a 1
            validando_status.status=1
            db.session.commit()
            return redirect(url_for('acceso.dash'))
        return redirect(url_for('acceso.login'))
    return render_template('formularios/login.html', formulario=form)

@acceso.route('/admin/close')
@login_required
def cerrar_sesion():
    validando_status=Users.query.get(current_user.id) #Esto actualiza datos, el status de 1 a 0 para salir
    validando_status.status=0
    db.session.commit()
    logout_user()
    return redirect(url_for('acceso.login'))

@acceso.route('/panel')
@login_required
def dash():
    query=db.session.query(Categorias, Posts).join(Posts).all()
    return render_template('admin/dashboard.html', query=query)