from pyapi.models.employee import db, EmployeeModel
from flask import jsonify, make_response, request
from Practice.helpers.helpers_func import is_there_any_empty_fields, serialize_employee_tab




class EmployeeService:

    def get(self):
        employees = EmployeeModel.query.all()
        serialized=serialize_employee_tab(employees)
        return make_response(jsonify({'status': 200, 'data': serialized}))

    # тут делаем все проверки валидации (функции которых должны лежать в отделаной папке типа validate or helpers)

    def post(self, new_record):
        if not is_there_any_empty_fields(new_record):
            db.session.add(EmployeeModel(
                new_record[0]['last_name'],
                new_record[0]['first_name'],
                new_record[0]['date_of_birth'],
                new_record[0]['job_title'],
                new_record[0]['hire_date'],
                new_record[0]['dismissal_date'],
                new_record[0]['email'],
                new_record[0]['phone']
            ))
            db.session.commit()
            return make_response(jsonify({'status': 201}))
        else:
            return make_response(jsonify({'status': 204, 'message': "заполните все строки"}))

    def update (self, updated_data):
        EmployeeModel.query.filter_by(id=updated_data[0]['id']).update(
            {'last_name': updated_data[0]['last_name'],
             'first_name': updated_data[0]['first_name'],
             'date_of_birth': updated_data[0]['date_of_birth'],
             'job_title': updated_data[0]['job_title'],
             'hire_date': updated_data[0]['hire_date'],
             'dismissal_date': updated_data[0]['dismissal_date'],
             'email': updated_data[0]['email'],
             'phone': updated_data[0]['phone']}
        )
        db.session.commit()
        return updated_data # зачем?

    def delete (self, delete_record):
        EmployeeModel.query.filter_by(id=delete_record[0]['id']).delete() # не уверен что это рабочая схема
        # db.session.delete(EmployeeModel(
        #     last_name=delete_record[0]['last_name'],
        #     first_name=delete_record[0]['first_name'],
        #     date_of_birth=date(delete_record[0]['date_of_birth']),
        #     job_title=delete_record[0]['job_title'],
        #     hire_date=date(delete_record[0]['hire_date']),
        #     dismissal_date=date(delete_record[0]['dismissal_date']),
        #     email=delete_record[0]['email'],
        #     phone=delete_record[0]['phone']
        # ))
        db.session.commit()

