from flask import Flask, request
from models.employee import db
from flask_cors import CORS
from service.employeeService import EmployeeService
from service.userService import UserService
from flask_jwt_extended import jwt_required

app = Flask(__name__)
db.init_app(app)
CORS(app)
employeeService = EmployeeService()
userService = UserService()


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'employee.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '12345'


@app.before_first_request
def create_tables():
    db.create_all()


@app.route("/api/v1/employees", methods=['GET'])
@jwt_required
def get_employees():
    return employeeService.get()


@app.route("/api/v1/employees/<id>", methods=['GET'])
@jwt_required
def get_employee(id):
    return employeeService.detail(id)


@app.route('/api/v1/employees/create', methods=['POST'])
@jwt_required
def create_employee():
    return employeeService.post(request.get_json())


@app.route('/api/v1/employees/update', methods=['PUT'])
@jwt_required
def update():
    print('methon put employee', request.get_json())
    return employeeService.update(request.get_json())


@ app.route('/api/v1/employees/delete', methods=['DELETE'])
@jwt_required
def delete():
    return employeeService.delete(request.get_json()['id'])


@app.route('/reg', methods=['POST'])
def register():
    return userService.registration()


@app.route('/log', methods=['POST'])
def login():
    return userService.login()


if __name__ == '__main__':
    app.run()
