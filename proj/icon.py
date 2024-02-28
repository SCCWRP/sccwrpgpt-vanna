import os
from flask import Blueprint, make_response
from .utils.vanna import vn

icon_bp = Blueprint('icon_bp', __name__)

@icon_bp.route('/icon')
def send_icon():
    #iconpath = os.path.join( os.getcwd() , 'static/vanna.svg' ) ## not working incorrect getcwd
    iconpath = os.path.join( '/home/app/proj/' , 'static/vanna.svg' ) ## not working incorrect getcwd
    #/home/app/static/vanna.svg
    #/home/app/proj/static/vanna.svg
    with open(iconpath, 'r') as iconfile:
        iconbinary = iconfile.read()

    response = make_response(iconbinary)
    response.headers.set('Content-Type', 'image/svg+xml')  # Adjust the MIME type as needed
    return response
