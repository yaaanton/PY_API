from flask import Flask, make_response, jsonify,request
from sqlalchemy import update,delete, MetaData,create_engine, Table
from datetime import  date


def serialize_employee_tab(employee_list):
    serialized = []
    for employee_list in employee_list:
        serialized.append({
            'id': employee_list[0],
            'last_name': employee_list[1],
            'first_name': employee_list[2],
            'date_of_birth': employee_list[3],
            'job_title': employee_list[4],
            'hire_date': employee_list[5],
            'dismissal_date': employee_list[6],
            'email': employee_list[7],
            'phone': employee_list[8],
        })
    return serialized


def show_employee_tab(db_name, tab_name):
    metadata = MetaData()
    engine = create_engine(f'sqlite:///{db_name}.db')
    emplist = Table(f'{tab_name}', metadata, autoload_with=engine)
    conn = engine.connect()
    req=emplist.select()
    res = conn.execute(req)
    employeetab = res.fetchall()
    result = serialize_employee_tab(employeetab)
    return result


def is_there_any_empty_fields(record):
    if record[0]['last_name'] != '' and record[0]['first_name'] != ''\
        and date(record[0]['date_of_birth']) != '' and record[0]['job_title'] != ''\
        and date(record[0]['hire_date']) != '' and date(record[0]['dismissal_date']) != ''\
        and record[0]['email'] != '' and record[0]['phone'] != '':
        return False
    else:
        return True


def append_record(db_name, tab_name, new_record):
    metadata = MetaData()
    engine = create_engine(f'sqlite:///{db_name}.db')
    emplist = Table(f'{tab_name}', metadata, autoload_with=engine)
    conn = engine.connect()
    ins = emplist.insert().values(
        last_name=new_record[0]['last_name'],
        first_name=new_record[0]['first_name'],
        date_of_birth=date(new_record[0]['date_of_birth']),
        job_title=new_record[0]['job_title'],
        hire_date=date(new_record[0]['hire_date']),
        dismissal_date=date(new_record[0]['dismissal_date']),
        email=new_record[0]['email'],
        phone=new_record[0]['phone']
    )
    conn.execute(ins)


def edit_record(db_name, tab_name, edited_record):
    metadata = MetaData()
    engine = create_engine(f'sqlite:///{db_name}.db')
    emplist = Table(f'{tab_name}', metadata, autoload_with=engine)
    conn = engine.connect()
    req = update(emplist).where(emplist.c.id == edited_record[0]['id']
    ).values(
        last_name=edited_record [0]['last_name'],
        first_name=edited_record [0]['first_name'],
        date_of_birth=date(edited_record [0]['date_of_birth']),
        job_title=edited_record [0]['job_title'],
        hire_date=date(edited_record [0]['hire_date']),
        dismissal_date=date(edited_record [0]['dismissal_date']),
        email=edited_record[0]['email'],
        phone=edited_record[0]['phone']
    )
    conn.execute(req)


def delete_record(db_name, tab_name, deleted_record):
    metadata = MetaData()
    engine = create_engine(f'sqlite:///{db_name}.db')
    emplist = Table(f'{tab_name}', metadata, autoload_with=engine)
    conn = engine.connect()
    req = delete(emplist).where(emplist.c.id == deleted_record[0]['id'])
    conn.execute(req)


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/api/v1/read/', methods=['GET'])# вывод всex
def read_api():
    result = show_employee_tab('Employee', 'Employee_list')
    return make_response(jsonify(result), 200)


@app.route('/api/v1/create', methods=['POST'])# добавление
def create_api():
    new_record = request.get_json()
    if not is_there_any_empty_fields():
        append_record('Employee', 'Employee_list', new_record)
        return make_response(jsonify(new_record), 201)
    else:
        return jsonify({'status': 204, 'message': "Заполните все поля"})


@app.route('/api/v1/update', methods=['PUT'])
def update_api():
    edited_record = request.get_json()
    edit_record('Employee', 'Employee_list',)
    return make_response(jsonify(edited_record), 204)


@app.route('/api/v1/delete', methods=['DELETE'])
def delete_api():
    deleted_record = request.get_json()
    delete_record('Employee', 'Employee_list', deleted_record)
    return 200


if __name__ == "__main__":
    app.run(debug=True)
