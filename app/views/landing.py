
from flask import Blueprint, render_template

landing = Blueprint('landing', __name__)


@landing.route('')
def index():
    return render_template('landing.html', name='davidkoojohn')


@landing.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@landing.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500