from file_host_app import db

class FileBase(db.Model):
    """
    """

    file_id = db.Column(db.Integer, primary_key = True)
    original_name = db.Column(db.String(64), index = True, nullable=False)	
    user_id  = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    permission_of_file = db.Colum(db.Enum('private', 'link', 'pablic', name = 'permission_of_file'), default = 'privat')	
    file_path = db.Column(db.String(80), nullable=False)
    count_download = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<File %r>' % (self.original_name)