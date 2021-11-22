from file_host_app import db

from werkzeug.security import check_password_hash, generate_password_hash
# from flask import current_app


class User(db.Model):
    """
    a table for saving users
    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(64))

    @classmethod
    def create_user(cls, username, password):
        new_user = User(username=username, password_hash=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()

    
    
    
    def __repr__(self):
        return '<User %r>' % (self.username)