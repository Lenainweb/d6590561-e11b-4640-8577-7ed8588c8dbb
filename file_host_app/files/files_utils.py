import uuid
from zipfile import ZipFile
from file_host_app import db
from file_host_app.config import Config
from .models import FileBase, UserLinks


def data_of_pablic_files():
    """
    Returns data about all public files.
    """
    files = FileBase.query.filter_by(permission_of_file='pablic').order_by(FileBase.count_download.desc()).all()
    # db = get_db()  
    # files = db.execute(
    #   'SELECT file_id, original_name, permission_of_file,file_path '
    #   ' FROM file_base WHERE permission_of_file="pablic" ORDER BY count_download DESC'
    #   ).fetchall()
    
    return files

def allowed_file(filename):
    """
    Allowed file.
    """

    return '.' in filename and \
        filename.rsplit('.', 1)[1] in Config.ALLOWED_EXTENSIONS

def get_name_uuid():
    """
    Generates a unique name to store the file.
    """

    return str(uuid.uuid4())  

def upload_file(original_name, user_id, permission_of_file, file_path):
    """
    Saving data about a new file in the database.
    """

    # db = get_db()
    # db.execute(
    #     'INSERT INTO file_base (original_name, user_id, permission_of_file, file_path)'
    #     ' VALUES (?, ?, ?,?)',
    #     (original_name, user_id, permission_of_file, file_path)
    # )
    # db.commit()
    new_file = FileBase(original_name=original_name, user_id=user_id, permission_of_file=permission_of_file, file_path=file_path)
    db.session.add(new_file)
    db.session.commit()         

def count_downloaded(file_id):
    """
    Link clicks counter.
    """

    # db = get_db()
    # db.execute(
    #     ' UPDATE file_base SET count_download = count_download + 1' 
    #     ' WHERE file_id = ?', (file_id,))
    # db.commit()
    file = FileBase.query.filter_by(file_id=file_id).first()
    file.count_download = FileBase.count_download + 1
    db.session.commit()
    



def download_file(file_id):
    """
    Returns data about a file from the database.
    """

    # db = get_db()    
    # file = db.execute(
    #     ' SELECT original_name, permission_of_file, file_path, user_id ' 
    #     ' FROM file_base WHERE file_id = ?',(file_id,)).fetchone()
    
    # return file
    file = FileBase.query.filter_by(file_id=file_id).first()
    return file
   
def check_access_by_link(user_id, file_id):
    """
    Checks if the link was available to the given user.
    """

    # db = get_db()
    # existing_entry = db.execute('SELECT user_id FROM user_links' 
    # 'WHERE (user_id = ?) AND  (fileid_id = ?) ',(user_id, file_id, )).fetchone()

    # return existing_entry


def create_access_by_link(user_id, file_id):
    """
    Add link access record to database.
    """

    # db = get_db()
    # db.execute(
    #         'INSERT INTO user_links (user_id, fileid_id)'
    #         ' VALUES (?, ?)',
    #         (user_id, file_id))
    # db.commit()
    new_link = UserLinks(user_id=user_id, file_id=file_id)
    db.session.add(new_link)
    db.session.commit()


def data_of_user_files():
    """
    Returns information about files uploaded by this user.
    """

    # db = get_db()
    # files = db.execute(
    #   'SELECT file_id, original_name, permission_of_file, file_path '
    #     ' FROM file_base f JOIN user u  ON f.user_id = u.id' 
    #     ' ORDER BY count_download DESC').fetchall()

    # return files

def data_of_links_users(user_id):
    """
    Returns information about files available through a link for a given user.
    """    
    # db = get_db()      
    # files = db.execute('SELECT file_id, original_name, permission_of_file,file_path' 
    #     ' FROM file_base WHERE file_id IN (SELECT fileid_id FROM user_links WHERE user_id=?)' 
    #     ' ORDER BY count_download DESC', (user_id,)
    #     ).fetchall()

    # return files

# async def make_zip():
#     """
#     """

#     db = get_db()    
#     file = db.execute(
#         ' SELECT original_name, permission_of_file, file_path, user_id ' 
#         ' FROM file_base').fetchone()

#     with ZipFile("test.zip", "w") as newzip:
#         newzip.write(Config.UPLOAD_FOLDER+'/'+file[2])


    

