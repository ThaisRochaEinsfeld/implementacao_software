from flask import Blueprint, render_template
from ..models import User, db

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/')

def index():
    usuarios = User.query.all() #['Thais', 'Pedro', 'Vi']
    return render_template("index.html", usuarios=usuarios)

@hello_bp.route('/sobre')

def about():
    return "Meu nome é Thais"

@hello_bp.route('/teste')

def test():
    return "Nova rota teste"