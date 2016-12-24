from app import *
from sqlalchemy import Column, String, Integer

# Define a User model
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, primary_key=True)
    role = db.Column(db.Integer)
    username = db.Column(db.String(128))
    email = db.Column(db.String(128))
    password = db.Column(db.String(128))
    phone = db.Column(db.String(128))
    created_at = db.Column(db.DateTime)

    def __init__(self, role, username, email, password, phone):
        self.role = role
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.created_at = datetime.utcnow()

    def verify_password(self, password):
        if(self.password == password):
            return True
        return False

    def __repr__(self):
        return '<User %r>' % (self.username)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
