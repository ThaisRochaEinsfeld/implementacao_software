from flask import Blueprint

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/')

def index():
    return "Olá, Mundo!"

@hello_bp.route('/sobre')

def about():
    return "Meu nome é Thais"