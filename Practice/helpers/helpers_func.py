from flask import Flask, make_response, jsonify,request
from sqlalchemy import update,delete, MetaData,create_engine, Table
from datetime import date


# def serialize_employee_tab(employee_list):
#     serialized = []
#     for employee_list in employee_list:
#         serialized.append({
#             'id': employee_list.id,
#             'last_name': employee_list.last_name,
#             'first_name': employee_list.first_name,
#             'date_of_birth': employee_list.date_of_birth,
#             'job_title': employee_list.job_title,
#             'hire_date': employee_list.hire_date,
#             'dismissal_date': employee_list.dismissal_date,
#             'email': employee_list.email,
#             'phone': employee_list.phone,
#         })
#     return serialized


def is_there_any_empty_fields(record):
    if record[0]['last_name'] != '' and record[0]['first_name'] != ''\
        and record[0]['date_of_birth'] != '' and record[0]['job_title'] != ''\
        and record[0]['hire_date'] != '' and record[0]['dismissal_date'] != ''\
        and record[0]['email'] != '' and record[0]['phone'] != '':
        return False
    else:
        return True

