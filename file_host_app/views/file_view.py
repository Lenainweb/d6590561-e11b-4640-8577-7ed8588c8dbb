from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, send_from_directory
)

from file_host_app.auth import login_required
from ..config import UPLOAD_FOLDER
from utils import utils_file

bp = Blueprint('file_host', __name__)

@bp.route('/')
def index():
    """
    main page with a list of all public files 
    """
    
    files =  utils_file.data_of_pablic_files()  
    
    return render_template('file_host/index.html', files=files)


@bp.route('/upload', methods=('GET', 'POST'))
@login_required
def upload():
    """ 
    page with a file adding form 
    """

    if request.method == 'GET':
        return render_template('file_host/upload.html')  
    
    file = request.files['file']

    if file and utils_file.allowed_file(file.filename):
        original_name = file.filename
        permission_of_file = request.form['permission']	
        file_path = utils_file.get_name_uuid()
        file.save(UPLOAD_FOLDER+'/'+file_path)
        
        utils_file.upload_file(original_name, g.user['id'], permission_of_file, file_path)
        
        return redirect(url_for('file_host.index'))

    if not file:
        flash('File is required.')

@bp.route('/download/<path:file_id>', methods=['GET', 'POST'])
@login_required
def download(file_id):
    """ 
    file download  
    """
    
    file_id = file_id
    error = None
    
    file = utils_file.download_file(file_id)
    
    if file[3] == g.user['id']:
        utils_file.count_downloaded(file_id)
        
        return send_from_directory(UPLOAD_FOLDER, file[2], attachment_filename=file[0], as_attachment=True)

    if file[1] != 'private':
        existing_entry = utils_file.check_access_by_link(g.user['id'], file_id)

        if existing_entry is None:
            utils_file.create_access_by_link(g.user['id'], file_id)
        utils_file.count_downloaded(file_id)
        
        return send_from_directory(UPLOAD_FOLDER, file[2], attachment_filename=file[0], as_attachment=True)
    
    flash('No permission to download the file.')


@bp.route('/my_files')
@login_required
def my_files():
    """ 
    displays a list of files uploaded by the user 
    """
    files = utils_file.data_of_user_files()
    
    return render_template('file_host/my_files.html', files=files)


@bp.route('/my_links')
@login_required
def my_links():
    """
    displays a list of files the user has access to
    """

    files = utils_file.data_of_links_users(g.user['id'])
        
    return render_template('file_host/my_links.html', files=files)
