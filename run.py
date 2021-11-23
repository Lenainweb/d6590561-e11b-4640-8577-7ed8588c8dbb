from flask.cli import with_appcontext
from flask_admin import Admin


from file_host_app import db
from file_host_app import create_app

from flask_admin.contrib.sqla import ModelView


from file_host_app.config import Config
from file_host_app.auth.models import User
from file_host_app.files.models import FileBase

app = create_app(Config)

@app.cli.command('init-db')
@with_appcontext
def initdb():
    db.drop_all()
    print("drop")
    db.create_all()
    print('Initialized the database.')

admin = Admin(app, name='file_host', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(FileBase, db.session))

if __name__ == "__main__":
    app.run()