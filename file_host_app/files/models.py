from file_host_app import db

class FileBase(db.Model):
    """
    """
    __tablename__ = 'file_base'

    file_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    original_name = db.Column(db.String(64), nullable=False)	
    user_id  = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    permission_of_file = db.Column(db.Enum('private', 'link', 'pablic', name = 'permission_of_file'), default = 'privat')	
    file_path = db.Column(db.String(80), nullable=False)
    count_download = db.Column(db.Integer, default=0)
    link = db.relationship('UserLinks', backref='links_for_user', lazy='dynamic')

    def __repr__(self):
        return '<File %r>' % (self.original_name)


class UserLinks(db.Model):
    """
    """
    __tablename__ = 'user_links'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    file_id = db.Column(db.Integer,db.ForeignKey('file_base.file_id'), nullable=False)
