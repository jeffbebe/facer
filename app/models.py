from app import db

from sqlalchemy import ForeignKey


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    sub = db.Column(db.String(255), unique=True)

    def __init__(self, sub, email):
        self.sub = sub
        self.email = email

    def __repr__(self):
        return "<User(id='%s', email='%s', sub='%s')>" % (
            self.user_id, self.email, self.sub)


class Image(db.Model):
    __tablename__ = 'images'
    image_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    filename = db.Column(db.String(255), unique=True)
    encoding = db.Column(db.LargeBinary(255))
    owner_id = db.Column(db.Integer, ForeignKey('users.user_id'))

    def __init__(self, name, filename, encoding, owner_id):
        self.name = name
        self.filename = filename
        self.encoding = encoding
        self.owner_id = owner_id
