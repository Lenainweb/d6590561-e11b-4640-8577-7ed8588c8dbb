# import uuid

# from flask import (
#     Blueprint, flash, g, redirect, render_template, request, url_for, send_from_directory
# )

# from file_host_app.auth import login_required
# from file_host_app.db import get_db
# from .config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS

# bp = Blueprint('file_host', __name__)


# @bp.route('/')
# def index():
#     """
#     main page with a list of all public files 
#     """
    
#     db = get_db()  
#     files = db.execute(
#       'SELECT file_id, original_name, permission_of_file,file_path '
#       ' FROM file_base WHERE permission_of_file="pablic" ORDER BY count_download DESC').fetchall()   
    
#     return render_template('file_host/index.html', files=files)


# @bp.route('/upload', methods=('GET', 'POST'))
# @login_required
# def upload():
#     """ 
#     page with a file adding form 
#     """

#     def allowed_file(filename):
#         return '.' in filename and \
#            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#     def get_name_uuid():
#         return str(uuid.uuid4())  

#     if request.method == 'POST':
#         file = request.files['file']
#         error = None

#         if file and allowed_file(file.filename):
#             original_name = file.filename
#             permission_of_file = request.form['permission']	
#             file_path = get_name_uuid()
#             file.save(UPLOAD_FOLDER+'/'+file_path)
#             db = get_db()
#             db.execute(
#                 'INSERT INTO file_base (original_name, user_id, permission_of_file, file_path)'
#                 ' VALUES (?, ?, ?,?)',
#                 (original_name, g.user['id'], permission_of_file, file_path)
#             )
#             db.commit()
            
#             return redirect(url_for('file_host.index'))

#         if not file:
#             error = 'File is required.'

#         if error is not None:
#             flash(error)          
    
#     return render_template('file_host/upload.html')


# def count_downloaded(file_id):
#     """
#     link clicks counter
#     """
#     db = get_db()
#     db.execute('UPDATE file_base SET count_download = count_download + 1 WHERE file_id = ?', (file_id,))
#     db.commit()


# @bp.route('/download/<path:file_id>', methods=['GET', 'POST'])
# @login_required
# def download(file_id):
#     """ 
#     file download  
#     """
    
#     file_id = file_id
#     error = None
#     db = get_db()    
#     file = db.execute(
#       'SELECT original_name, permission_of_file, file_path, user_id FROM file_base WHERE file_id = ?',(file_id,)).fetchone()

#     if file[3] == g.user['id']:
#         count_downloaded(file_id)
        
#         return send_from_directory(UPLOAD_FOLDER, file[2], attachment_filename=file[0], as_attachment=True)

#     elif file[1] != 'private':
#         existing_entry = db.execute('SELECT user_id FROM user_links' 
#         'WHERE (user_id = ?) AND  (fileid_id = ?) ',(g.user['id'], file_id, )).fetchone()

#         if existing_entry is None:
#             db = get_db()
#             db.execute(
#                     'INSERT INTO user_links (user_id, fileid_id)'
#                     ' VALUES (?, ?)',
#                     (g.user['id'], file_id))
#             db.commit()
#         count_downloaded(file_id)
        
#         return send_from_directory(UPLOAD_FOLDER, file[2], attachment_filename=file[0], as_attachment=True)

#     else:
#         error = 'No permission to download the file.'
#     flash(error)


# @bp.route('/my_files')
# @login_required
# def my_files():
#     """ 
#     displays a list of files uploaded by the user 
#     """
#     db = get_db()
#     error = None

#     files = db.execute(
#       'SELECT file_id, original_name, permission_of_file, file_path '
#       'FROM file_base f JOIN user u  ON f.user_id = u.id ORDER BY count_download DESC').fetchall()
    
#     return render_template('file_host/my_files.html', files=files)


# @bp.route('/my_links')
# @login_required
# def my_links():
#     """
#     displays a list of files the user has access to
#     """
    
#     db = get_db()
      
#     files = db.execute('SELECT file_id, original_name, permission_of_file,file_path FROM file_base WHERE file_id IN (SELECT fileid_id FROM user_links WHERE user_id=?)' 
#     'ORDER BY count_download DESC', (g.user['id'],)
#     ).fetchall()
    
#     return render_template('file_host/my_links.html', files=files)
