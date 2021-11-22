import click
from flask.cli import with_appcontext

from file_host_app import db
from file_host_app import create_app

from file_host_app.config import Config

app = create_app(Config)

# @app.cli.command("init_db")

@app.cli.command('init-db')
@with_appcontext
def initdb():
    db.drop_all()
    print("drop")
    db.create_all()
    # @click.command('init-db')
# @with_appcontext
# def init_db_command():
#     """Clear the existing data and create new tables."""
#     init_db()
    print('Initialized the database.')
    

if __name__ == "__main__":
    app.run()