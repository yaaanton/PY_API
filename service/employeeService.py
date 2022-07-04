from hashlib import new
from models.employee import db, EmployeeModel
from flask import jsonify, make_response


class EmployeeService:

    def get(self):
        employees = EmployeeModel.query.all()
        return make_response(jsonify({'status': 200, 'data': EmployeeModel.serialize_list(employees)}))

    def post(self, data_request):
        new_employees = EmployeeModel(**data_request)
        db.session.add(new_employees)
        db.session.commit()
        return make_response(jsonify({'status': 201}))

    def detail(self, id):
        employee = EmployeeModel.query.get(id)
        return make_response(jsonify({'status': 200, 'data': EmployeeModel.serialize(employee)}))

    def update(self, data):
        id = data['id']
        employee_fields = data['employee']
        current_employee = EmployeeModel.query.filter_by(id=id).update(
            {'first_name': employee_fields['first_name'],
             'second_name': employee_fields['second_name'],
             'date_of_birth': employee_fields['date_of_birth'],
             'job_title': employee_fields['job_title'],
             'hire_date': employee_fields['hire_date'],
             'dismissal_date': employee_fields['dismissal_date'],
             'email': employee_fields['email'],
             'phone': employee_fields['phone']}
        )
        # db.session.add(current_employee)
        db.session.commit()
        return make_response(jsonify({'status': 204}))

    def delete(self, id):
        employee = EmployeeModel.query.get(id)
        db.session.delete(employee)
        db.session.commit()
        return make_response(jsonify({'status': 200}))
