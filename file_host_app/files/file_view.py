from flask import (
    flash, g, redirect, render_template, request, url_for, send_from_directory
)

from auth.auth_utils import login_required
from config import UPLOAD_FOLDER
from . import file_host as bp
from files import files_utils


@bp.route('/')
def index():
    """
    main page with a list of all public files 
    """
    
    files = files_utils.data_of_pablic_files()  

    return render_template('file_host/index.html', files=files)


@bp.route('/upload', methods=('GET',))
@login_required
def upload_get():
    """ 
    page with a file adding form 
    """

    return render_template('file_host/upload.html')  
    

@bp.route('/upload', methods=('POST',))
@login_required
def upload():
    """ 
    page with a file adding form 
    """

    file = request.files['file']

    if file and files_utils.allowed_file(file.filename):
        original_name = file.filename
        permission_of_file = request.form['permission']	
        file_path = files_utils.get_name_uuid()
        file.save(UPLOAD_FOLDER+'/'+file_path)
        
        files_utils.upload_file(original_name, g.user['id'], 
            permission_of_file, file_path)
        
        return redirect(url_for('file_host.index'))

    if not file:
        flash('File is required.')


@bp.route('/download/<path:file_id>', methods=['POST',])
@login_required
def download(file_id):
    """ 
    file download  
    """
    
    file_id = file_id
    
    file = files_utils.download_file(file_id)
    
    if file[3] == g.user['id']:
        files_utils.count_downloaded(file_id)
        
        return send_from_directory(UPLOAD_FOLDER, file[2], 
            attachment_filename=file[0], 
            as_attachment=True)

    if file[1] != 'private':
        existing_entry = files_utils.check_access_by_link(g.user['id'], file_id)

        if existing_entry is None:
            files_utils.create_access_by_link(g.user['id'], file_id)
        files_utils.count_downloaded(file_id)
        
        return send_from_directory(UPLOAD_FOLDER, file[2], 
            attachment_filename=file[0], 
            as_attachment=True)
    
    flash('No permission to download the file.')


@bp.route('/my_files')
@login_required
def my_files():
    """ 
    displays a list of files uploaded by the user 
    """
    files = files_utils.data_of_user_files()
    
    return render_template('file_host/my_files.html', files=files)


@bp.route('/my_links')
@login_required
def my_links():
    """
    displays a list of files the user has access to
    """

    files = files_utils.data_of_links_users(g.user['id'])
        
    return render_template('file_host/my_links.html', files=files)


@bp.route('/download/part', methods=['POST',])
@login_required
def download_part_files():
    """ 
    download archive  
    """
    pass
        
   
