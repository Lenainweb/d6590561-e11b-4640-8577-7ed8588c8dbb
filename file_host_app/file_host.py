from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from file_host_app.auth import login_required
from file_host_app.db import get_db

bp = Blueprint('file_host', __name__)

@bp.route('/')
def index():
    db = get_db()
    files = db.execute(
        'SELECT f.id, original_filename, onwer_id, owner'
        ' FROM file f JOIN user u ON f.onwer_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', files=files)

# @bp.route('/upload', methods=('GET', 'POST', 'FILE'))
# @login_required
# def upload():
#     if request.method == 'FILE':
#         file = request.form['file']
#         permission_for_file = request.form['permission_for_file']
#         error = None

#         if not file:
#             error = 'File is required.'

#         if error is not None:
#             flash(error)
#         else:
#             db = get_db()
#             db.execute(
#                 'INSERT INTO file (title, body, author_id)'
#                 ' VALUES (?, ?, ?)',
#                 (title, body, g.user['id'])
#             )
#             db.commit()
#             return redirect(url_for('file_host.index'))

#     return render_template('file_host/upload.html')