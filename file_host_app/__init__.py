import os
import click
from flask.cli import with_appcontext

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from config import SQLALCHEMY_DATABASE_URI
# from config import Config

db = SQLAlchemy()

# @click.command('init-db')
# @with_appcontext
# def initdb():
#     db.drop_all()
#     db.create_all()

# app.config.from_object(Config)

def create_app(config):
    # create and configure the app
    app = Flask(__name__)

    # app.config.from_object(config)
    app.config['SECRET_KEY'] = 'key'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'app.db') 

    db.init_app(app)

    from file_host_app.auth import auth as auth_bp
    app.register_blueprint(auth_bp)

    from file_host_app.files import file_host as files_bp
    app.register_blueprint(files_bp)
    app.add_url_rule('/', endpoint='index')
    
    # return app
    from file_host_app.auth import models, auth_view, auth_utils
    from file_host_app.files import models, file_view, files_utils

    # with app.app_context(): 
    #     db.create_all()

    return app








# from app import views, models