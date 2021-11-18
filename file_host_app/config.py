import os

SECRET_KEY = 'secret_key'

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

UPLOAD_FOLDER = os.path.join(basedir, 'static/upload')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
