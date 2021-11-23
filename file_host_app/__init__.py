import os
import click
from flask.cli import with_appcontext

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config):
    # create and configure the app
    app = Flask(__name__)

    # app.config.from_object(config)
    app.config['SECRET_KEY'] = 'key'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'app.db') 
    app.config['FLASK_ADMIN_SWATCH'] = '007'

    db.init_app(app)

    from file_host_app.auth import auth as auth_bp
    app.register_blueprint(auth_bp)

    from file_host_app.files import file_host as files_bp
    app.register_blueprint(files_bp)
    app.add_url_rule('/', endpoint='index')
    
    from file_host_app.auth import models, auth_view, auth_utils
    from file_host_app.files import models, file_view, files_utils

    return app
