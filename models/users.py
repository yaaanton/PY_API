from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import create_access_token
from passlib.hash import bcrypt

db = SQLAlchemy()


class UsersModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)

    def __init__(self,  email, password):
        self.email = email
        self.password = bcrypt.hash(password)

    def get_token(self):
        token = create_access_token(identity=self.id)
        return token

    @classmethod
    def authentication(cls, email, password):
        user = cls.query.filter(cls.email == email).one()
        if not bcrypt.verify(password, user.password):
            raise Exception('wrong password')
        return user


