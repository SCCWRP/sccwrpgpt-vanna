import os
from flask import Flask, jsonify, Response, request, redirect, url_for, send_file, make_response
from functools import wraps

from .download import download_bp 
from .icon import icon_bp
from .index import index_bp
from .plots import plots_bp
from .questions import questions_bp
from .sql import sql_bp
from .training import training_bp


app = Flask(__name__, static_url_path='', static_folder='static')

print("### STARTING FLASK App ###")


app.register_blueprint(download_bp )
app.register_blueprint(icon_bp)
app.register_blueprint(index_bp)
app.register_blueprint(plots_bp)
app.register_blueprint(questions_bp)
app.register_blueprint(sql_bp)
app.register_blueprint(training_bp)


