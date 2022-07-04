from flask_sqlalchemy import SQLAlchemy
from models.serializer import Serializer
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class EmployeeModel(db.Model, Serializer):
    __tablename__ = "employee"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    first_name = db.Column(db.String(255))
    second_name = db.Column(db.String(255))
    date_of_birth = db.Column(db.String())
    job_title = db.Column(db.String(255))
    hire_date = db.Column(db.String())
    dismissal_date = db.Column(db.Integer())
    email = db.Column(db.String(255))
    phone = db.Column(db.String(255))

    def __init__(self, first_name, second_name, date_of_birth, job_title, hire_date, dismissal_date, email, phone):
        self.first_name = first_name
        self.second_name = second_name
        self.date_of_birth = date_of_birth
        self.job_title = job_title
        self.hire_date = hire_date
        self.dismissal_date = dismissal_date
        self.email = email
        self.phone = phone

    def serialize(self):
        d = Serializer.serialize(self)
        return d

    def __repr__(self):
        return f"{self.first_name}:{self.second_name}"
