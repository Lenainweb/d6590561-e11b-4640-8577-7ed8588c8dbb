from file_host_app import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import current_app


class User(db.Model):
    """
    a table for saving users
    """

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True, nullable=False)
    password_hash = db.Column(db.String(64))

    @property
    def password(self):
        raise AttributeError('`password` is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


    def __repr__(self):
        return '<User %r>' % (self.username)