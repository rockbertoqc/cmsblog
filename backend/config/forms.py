from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, SubmitField, StringField, SelectField, SearchField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField

class Login(FlaskForm):
    username=StringField('Ingresa nombre de usuario', validators=[DataRequired()])
    password=PasswordField('Ingresa contraseña', validators=[DataRequired()])
    submit=SubmitField('Entrar')

# Instanciamos esta clase en category.py como form y la pasamos como formulario al jinja2 
class FormularioCategorias(FlaskForm):
    categoria=StringField('Categoría', validators=[DataRequired()])
    enviar=SubmitField('Aceptar')

class FormularioPosts(FlaskForm):
    titulo=StringField('Ingresa título', validators=[DataRequired()])
    body=CKEditorField('Escribe', validators=[DataRequired()])
    tags=StringField('Etiquetas', validators=[DataRequired()])
    categoria=SelectField('Categoría', choices=[], validators=[DataRequired()])
    enviar=SubmitField('Publicar')

class AddUser(FlaskForm):
    nombre=StringField('Nombre', validators=[DataRequired()])
    usuario=StringField('Nuevo usuario', validators=[DataRequired()])
    clave=StringField('Ingresa password', validators=[DataRequired()])
    correo=StringField('Ingresa e-mail', validators=[DataRequired()])
    enviar=SubmitField('Enviar')

class UpdateUser(FlaskForm):
    nombre=StringField('Nombre', validators=[DataRequired()])
    usuario=StringField('Nuevo usuario', validators=[DataRequired()])
    clave=StringField('Ingresa password', validators=[DataRequired()])
    correo=StringField('Ingresa e-mail', validators=[DataRequired()])
    enviar=SubmitField('Enviar')
