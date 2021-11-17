from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')

from . import auth_view, auth_utils
