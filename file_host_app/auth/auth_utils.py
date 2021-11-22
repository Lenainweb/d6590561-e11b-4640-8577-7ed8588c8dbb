import functools

from flask import g, redirect, url_for

from werkzeug.security import generate_password_hash

from .models import User

from file_host_app import db


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


# def create_user(username, password):
#     """
#     Creates a new user in the database.
#     """
#     # db = get_db()
#     # db.execute(
#     #     "INSERT INTO user (username, password) VALUES (?, ?)",
#     #     (username, generate_password_hash(password)),
#     # )
#     # db.commit()
    
#     new_user = User(username=username, password_hash=generate_password_hash(password))
#     db.session.add(new_user)
#     db.session.commit()


def data_of_user(username):
    """
    Returns data about the current user.
    """
    # db = get_db()
    # user = db.execute(
    #     'SELECT * FROM user WHERE username = ?', (username,)
    # ).fetchone()

    # return user
    return User.query.filter_by(username=username).first()


def load_user(user_id):
    """
    Places user information into a global variable.
    """
    # user = get_db().execute(
    #     'SELECT * FROM user WHERE id = ?', (user_id,)
    # ).fetchone()

    # return user
    return User.query.filter_by(id=user_id).first()

