from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, send_from_directory
)
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename

import uuid

from file_host_app.auth import login_required
from file_host_app.db import get_db
from .config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS

bp = Blueprint('file_host', __name__)


@bp.route('/')
def index():
    db = get_db()
  
    files = db.execute(
      'SELECT file_id, original_name, permission_of_file,file_path '
      ' FROM file_base WHERE permission_of_file="pablic" ORDER BY count_download DESC').fetchall()   
    return render_template('file_host/index.html', files=files)



@bp.route('/upload', methods=('GET', 'POST'))
@login_required
def upload():

    def allowed_file(filename):
        return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

    def get_name_uuid():
        return str(uuid.uuid4())  

    if request.method == 'POST':
        file = request.files['file']
        error = None

        if file and allowed_file(file.filename):
            original_name = file.filename
            # filename = secure_filename(file.filename)
            permission_of_file = request.form['permission']	
            file_path = get_name_uuid()
            file.save(UPLOAD_FOLDER+'/'+file_path)

            db = get_db()
            db.execute(
                'INSERT INTO file_base (original_name, user_id, permission_of_file, file_path)'
                ' VALUES (?, ?, ?,?)',
                (original_name, g.user['id'], permission_of_file, file_path)
            )
            db.commit()
            return redirect(url_for('file_host.index'))

        if not file:
            error = 'File is required.'

        if error is not None:
            flash(error)          
    return render_template('file_host/upload.html')

@bp.route('/download/<path:file_id>', methods=['GET', 'POST'])
@login_required
def download(file_id):
    file_id = file_id
    db = get_db()

    file = db.execute(
      'SELECT original_name, permission_of_file,file_path '
      ' FROM file_base WHERE file_id=1').fetchall() 
    
    directory = (UPLOAD_FOLDER+'/'+file['file_path']) 

    return send_from_directory(directory=directory, file_name=file.original_name)

@bp.route('/my_files')
@login_required
def my_files():
    db = get_db()
      
    files = db.execute(
      'SELECT file_id, original_name, permission_of_file, file_path '
      'FROM file_base f JOIN user u  ON f.user_id = u.id ORDER BY count_download DESC').fetchall()
    return render_template('file_host/my_files.html', files=files)

@bp.route('/my_links')
@login_required
def my_links():
    db = get_db()
  
    files = db.execute('SELECT file_id, original_name, permission_of_file,file_path  FROM file_base WHERE file_id IN (SELECT fileid_id FROM user_links WHERE user_id=1)'
    ).fetchall()
    return render_template('file_host/my_links.html', files=files)
