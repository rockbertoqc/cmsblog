from flask import Blueprint, url_for, render_template, redirect, request
from backend.config.settings import db
from backend.config.models import Categorias, Posts, Users
from datetime import datetime

blogview=Blueprint('blogview', __name__)

@blogview.route('/')
def index():
    consultas=db.session.query(Categorias, Posts).join(Posts).all()
    entradas=Posts.query.all()
    for consulta in consultas:
        categoria=consulta.Categorias.categoria
        titulo=consulta.Posts.titulo
        ruta=categoria.replace(' ', '-').lower() + "/" + titulo.replace(' ', '-').lower()
    return render_template('blog/index.html', consultas=consultas, ruta=ruta, entradas=entradas) 

@blogview.route('/entrada/<int:id>/<string:titulo>')
def single_post(id, titulo):
    #consulta=Posts.query.get(id)
    consulta=db.session.query(Categorias, Posts).join(Posts).filter_by(id=id).all()
    return render_template('blog/single.html', consulta=consulta)