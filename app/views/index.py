from flask import Blueprint, request, jsonify, render_template, g

import flask_sijax

app = Blueprint('index', __name__)

@flask_sijax.route(app, '/')
def index():
    return 'hello world!!', 200
