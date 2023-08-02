from backend.config.settings import db
from flask_login import UserMixin

class Users(UserMixin, db.Model):
    __tablename__='usuarios'
    id=db.Column(db.Integer(), primary_key=True)
    nombre=db.Column(db.String(255), nullable=False)
    usuario=db.Column(db.String(255), nullable=False, unique=True)
    clave=db.Column(db.String(255), nullable=False)
    correo=db.Column(db.String(255), nullable=False)
    status=db.Column(db.Integer(), default=0)
    rel=db.relationship('Posts', backref='usuarios')

class Categorias(db.Model):
    __tablename__='categorias'
    id=db.Column(db.Integer(), primary_key=True)
    categoria=db.Column(db.String(255), nullable=False)
    rel=db.relationship('Posts', backref='categorias')

class Posts(db.Model):
    __tablename__='entradas'
    id=db.Column(db.Integer(), primary_key=True)
    titulo=db.Column(db.Text(), nullable=False)
    body=db.Column(db.Text(), nullable=False)
    tags=db.Column(db.Text(), nullable=False)
    date=db.Column(db.Date(), nullable=False)
    id_usuario=db.Column(db.Integer(), db.ForeignKey('usuarios.id'))
    id_categoria=db.Column(db.Integer(), db.ForeignKey('categorias.id'))

    def __init__(self, titulo, body, tags, date, id_usuario, id_categoria):
        self.titulo=titulo
        self.body=body
        self.tags=tags
        self.date=date
        self.id_usuario=id_usuario
        self.id_categoria=id_categoria
    
    def __repr__(self):
        return '<Posts %r>' % self.titulo

    def uri_path(self):
        return self.titulo.replace(' ', '-').lower()