from requests import request
from models.users import db, UsersModel
from flask import jsonify


class UserService:

    @staticmethod
    def registration():
        data = request.json
        user = UsersModel(**data)
        db.session.add(user)
        db.session.commit()
        token = user.get_token()
        return jsonify({'access_token': token})

    @staticmethod
    def login():
        data = request.json
        user = UsersModel.authentication(**data)
        token = user.get_token
        return jsonify({'access_token': token})
