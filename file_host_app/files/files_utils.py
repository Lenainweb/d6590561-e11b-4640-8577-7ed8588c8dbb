from flask import g
import uuid
from zipfile import ZipFile
from file_host_app import db
from file_host_app.config import Config
from .models import FileBase, UserLinks


def data_of_pablic_files():
    """
    Returns data about all public files.
    """
    files = FileBase.query.filter_by(permission_of_file='pablic'
        ).order_by(FileBase.count_download.desc()).all()
        
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

    new_file = FileBase(
        original_name=original_name, 
        user_id=user_id, 
        permission_of_file=permission_of_file, 
        file_path=file_path)
    db.session.add(new_file)
    db.session.commit()         


def count_downloaded(file_id):
    """
    Link clicks counter.
    """

    file = FileBase.query.filter_by(file_id=file_id).first()
    file.count_download = FileBase.count_download + 1
    db.session.commit()
 

def download_file(file_id):
    """
    Returns data about a file from the database.
    """
    file = FileBase.query.filter_by(file_id=file_id).first()
    return file


def check_access_by_link(user_id, file_id):
    """
    Checks if the link was available to the given user.
    """

    # db = get_db()
    # existing_entry = db.execute('SELECT user_id FROM user_links' 
    # 'WHERE (user_id = ?) AND  (fileid_id = ?) ',(user_id, file_id, )).fetchone()
    
    existing_entry = UserLinks.query(user_id).filter_by(user_id=user_id).filter_by(file_id=file_id).first()

    return existing_entry


def create_access_by_link(user_id, file_id):
    """
    Add link access record to database.
    """

    new_link = UserLinks(user_id=user_id, file_id=file_id)
    db.session.add(new_link)
    db.session.commit()


def data_of_user_files():
    """
    Returns information about files uploaded by this user.
    """

    files = FileBase.query.filter_by(user_id=g.user.id).order_by(
        FileBase.count_download.desc()).all()

    return files

def data_of_links_users(user_id):
    """
    Returns information about files available through a link for a given user.
    """    
    
    files = FileBase.query.filter(UserLinks.user_id==g.user.id).all()
    return files

# async def make_zip():
#     """
#     """

#     db = get_db()    
#     file = db.execute(
#         ' SELECT original_name, permission_of_file, file_path, user_id ' 
#         ' FROM file_base').fetchone()

#     with ZipFile("test.zip", "w") as newzip:
#         newzip.write(Config.UPLOAD_FOLDER+'/'+file[2])


    

