
from flask import (
    g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash

from . import auth as bp
from . import auth_utils
from . import models


@bp.route('/register', methods=('GET', 'POST'))
def register():
    """
    user registration page 
    """

    if request.method == 'GET':
        
        return render_template('auth/register.html')
   
    username = request.form['username']
    password = request.form['password']
    error = None
    
    if not username:
        error = 'Username is required.'
    elif not password:
        error = 'Password is required.'

    if error is None:
        models.User.create_user(username, password)
        return redirect(url_for("auth.login"))
    else:
        return render_template('auth/register.html')



@bp.route('/login', methods=('GET', 'POST'))
def login():
    """ 
    user authentication page 
    """ 
    
    if request.method == 'GET':
        
        return render_template('auth/login.html')
        
    username = request.form['username']
    password = request.form['password']
    error = None
    user = auth_utils.data_of_user(username)

    if user is None:
        error = 'Incorrect username.'
    elif not check_password_hash(user.password_hash, password):
        error = 'Incorrect password.'

    if error is None:
        session.clear()
        session['user_id'] = user.id
        g.user = auth_utils.load_user(session.get('user_id'))
        return redirect(url_for('index'))


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = auth_utils.load_user(user_id)


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
