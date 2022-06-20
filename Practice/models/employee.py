from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class EmployeeModel(db.Model):
    __tablename__ = 'Employee_list'

    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(30), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    job_title = db.Column(db.String(20), nullable=False)
    hire_date = db.Column(db.Date, nullable=False)
    dismissal_date = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    def __init__(self, last_name, first_name, date_of_birth, job_title, hire_date, dismissal_date, email, phone):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.job_title = job_title
        self.hire_date = hire_date
        self.dismissal_date = dismissal_date
        self.email = email
        self.phone = phone

    def __repr__(self):

        pass
