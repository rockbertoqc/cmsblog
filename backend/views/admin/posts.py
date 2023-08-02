from flask import Blueprint, render_template, redirect, url_for, request
from backend.config.settings import db
from backend.config.models import Categorias, Posts, Users
from backend.config.forms import FormularioCategorias, FormularioPosts
from datetime import datetime
from flask_login import current_user, login_required

articulos = Blueprint('articulos', __name__)

@articulos.route('/entradas/agregar', methods=['GET', 'POST'])
@login_required
def agregar_entrada():
    form=FormularioPosts()
    lista_de_categorias=Categorias.query.all()
    form.categoria.choices=[(item.id, item.categoria) for item in lista_de_categorias]
    if form.validate_on_submit():
        fecha=datetime.now()
        insertar_entrada=Posts(
            titulo=form.titulo.data, 
            body=form.body.data, 
            tags=form.tags.data, 
            date=fecha, 
            id_usuario=current_user.id, 
            id_categoria=form.categoria.data)
        db.session.add(insertar_entrada)
        db.session.commit()
        return redirect(url_for('acceso.dash'))
    return render_template('admin/agregar_entrada.html', form=form, lista=lista_de_categorias)
    
@articulos.route('/entradas/borrar/<int:id>', methods=['GET', 'POST'])
@login_required
def borrar_entrada(id):
    queryu=Posts.query.get(id)
    db.session.delete(queryu)
    db.session.commit()
    return redirect(url_for('acceso.dash'))