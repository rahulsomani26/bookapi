from werkzeug.security import safe_str_cmp
from models.user import User


def authenticate(username, password):
    user = User.get_user_by_name(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    # This contains the content of the JSON web token
    user_id = payload['identity']
    return User.get_user_by_id(user_id)
