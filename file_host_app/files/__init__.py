from flask import Blueprint

file_host = Blueprint('file_host', __name__)

from . import file_view