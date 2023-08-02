from flask import Blueprint, render_template, redirect, url_for, request
from backend.config.settings import db
from backend.config.models import Categorias, Posts, Users
from backend.config.forms import FormularioCategorias, FormularioPosts
from datetime import datetime
from flask_login import current_user, login_required

categoria = Blueprint('categoria', __name__)

@categoria.route('/categoria/agregar', methods = ['GET', 'POST'])
@login_required
def agregar_categoria():
    mostrar_categorias=Categorias.query.all() #[select * from Categorias;]
    form=FormularioCategorias()
    if form.validate_on_submit():
        agregar_category=Categorias(categoria=form.categoria.data)
        db.session.add(agregar_category)
        db.session.commit()
        return redirect(url_for('categoria.agregar_categoria'))
    return render_template('admin/agregar_categoria.html', formulario=form, ver_categorias=mostrar_categorias)

@categoria.route('/categoria/borrar/<int:id>')
@login_required
def borrar_categoria(id):
    borrar=Categorias.query.get(id) # SELECT * FROM Categorias WHERE id = id;
    db.session.delete(borrar) # DELETE FROM Categorias WHERE id IN (SELECT * FROM Categorias WHERE id = id);
    db.session.commit()
    return redirect(url_for('categoria.agregar_categoria'))



