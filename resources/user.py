import sqlite3
from flask_restful import Resource, reqparse
from flask import Flask, request
from models.user import User


class RegisterdUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True,
                        help='Username required')
    parser.add_argument('password', type=str, required=True,
                        help='Password required')

    def post(self):
        # payload = request.get_json()  try using this aswell and see whether it works or not
        # add some code here

        payload = RegisterdUser.parser.parse_args()
        if User.get_user_by_name(payload['username']):
            return{"user already exists ": payload['username']}, 400

        con = sqlite3.connect('data.db')
        cur = con.cursor()
        cur.execute('insert into USERS values(null,?,?)',
                    (payload["username"], payload["password"]))
        con.commit()
        con.close()
        return "user created", 201
