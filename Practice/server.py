from flask import Flask, request, jsonify
from models.employee import db
from flask_cors import CORS
from pyapi.service.employeeService import EmployeeService

app = Flask(__name__)
db.init_app(app)
CORS(app)
employeeService = EmployeeService()


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Employee2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False


@app.before_first_request
def create_tables():
    db.create_all()


@app.route("/api/v1/employees", methods=['GET'])
def get_employees():
    return employeeService.get()


@app.route('/api/v1/employees/create', methods=['POST'])
def create_employee():
    return employeeService.post(request.get_json())


@app.route('/api/v1/employees/update', methods=['PUT'])
def edit_employee():
    return employeeService.update(request.get_json())


@app.route('/api/v1/employees/delete', methods=['DELETE'])
def delete_employee():
    employeeService.delete(request.get_json())
    return jsonify({"status": 200})


if __name__ == '__main__':
    app.run()
