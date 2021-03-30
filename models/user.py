import sqlite3


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def get_user_by_name(cls, username):
        # create a connection
        con = sqlite3.connect('data.db')
        # create a cursor object
        cur = con.cursor()

        # Fire sql query to insert values in the database
        result = cur.execute(
            'select * from USERS where username=?', (username,))
        row = result.fetchone()
        if row is not None:
            user = cls(row[0], row[1], row[2])

        else:
            user = None
        return user

    @classmethod
    def get_user_by_id(cls, _id):
        # create a connection
        con = sqlite3.connect('data.db')
        # create a cursor object
        cur = con.cursor()

        # Fire sql query to insert values in the database
        result = cur.execute(
            'select * from USERS where id=?', (_id,))
        row = result.fetchone()
        if row is not None:
            # user = cls(row[0], row[1], row[2])
            user = cls(*row)
        else:
            user = None
        return user
