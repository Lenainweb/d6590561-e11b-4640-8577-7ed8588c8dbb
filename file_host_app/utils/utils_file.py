import uuid
from file_host_app.db import get_db
from ..config import ALLOWED_EXTENSIONS

# def index():
def data_of_pablic_files():
    
    db = get_db()  
    files = db.execute(
      'SELECT file_id, original_name, permission_of_file,file_path '
      ' FROM file_base WHERE permission_of_file="pablic" ORDER BY count_download DESC').fetchall()
    
    return files

def allowed_file(filename):
    
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def get_name_uuid():
    
    return str(uuid.uuid4())  

# def upload():
def upload_file(original_name, user_id, permission_of_file, file_path):

    db = get_db()
    db.execute(
        'INSERT INTO file_base (original_name, user_id, permission_of_file, file_path)'
        ' VALUES (?, ?, ?,?)',
        (original_name, user_id, permission_of_file, file_path)
    )
    db.commit()         

def count_downloaded(file_id):
    """
    link clicks counter
    """
    db = get_db()
    db.execute('UPDATE file_base SET count_download = count_download + 1 WHERE file_id = ?', (file_id,))
    db.commit()



# def download(file_id):
def download_file(file_id):

    db = get_db()    
    file = db.execute(
      'SELECT original_name, permission_of_file, file_path, user_id FROM file_base WHERE file_id = ?',(file_id,)).fetchone()
    
    return file

    
def check_access_by_link(user_id, file_id):

    db = get_db()
    existing_entry = db.execute('SELECT user_id FROM user_links' 
    'WHERE (user_id = ?) AND  (fileid_id = ?) ',(user_id, file_id, )).fetchone()

    return existing_entry

def create_access_by_link(user_id, file_id):

    db = get_db()
    db.execute(
            'INSERT INTO user_links (user_id, fileid_id)'
            ' VALUES (?, ?)',
            (user_id, file_id))
    db.commit()


# def my_files():
def data_of_user_files():

    db = get_db()

    files = db.execute(
      'SELECT file_id, original_name, permission_of_file, file_path '
      'FROM file_base f JOIN user u  ON f.user_id = u.id ORDER BY count_download DESC').fetchall()

    return files



# def my_links():
def data_of_links_users(user_id):
    
    db = get_db()
      
    files = db.execute('SELECT file_id, original_name, permission_of_file,file_path FROM file_base WHERE file_id IN (SELECT fileid_id FROM user_links WHERE user_id=?)' 
    'ORDER BY count_download DESC', (user_id,)
    ).fetchall()

    return files
    