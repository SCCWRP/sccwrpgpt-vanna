from flask import Blueprint

index_bp = Blueprint('index_bp', __name__, static_folder='static')

@index_bp.route('/')
def root():
    return index_bp.send_static_file('index.html')