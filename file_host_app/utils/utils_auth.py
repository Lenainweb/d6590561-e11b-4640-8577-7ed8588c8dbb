from flask import g

from werkzeug.security import generate_password_hash

from file_host_app.db import get_db

def create_user(username, password):
    """
    Creates a new user in the database.
    """
    db = get_db()
    db.execute(
        "INSERT INTO user (username, password) VALUES (?, ?)",
        (username, generate_password_hash(password)),
    )
    db.commit()
            
# def login():
def data_of_user(username):
    """
    Returns data about the current user.
    """
    db = get_db()
    user = db.execute(
        'SELECT * FROM user WHERE username = ?', (username,)
    ).fetchone()
    
    return user

# def load_logged_in_user():
def load_user(user_id):
    """
    Places user information into a global variable.
    """
    g.user = get_db().execute(
        'SELECT * FROM user WHERE id = ?', (user_id,)
    ).fetchone()

