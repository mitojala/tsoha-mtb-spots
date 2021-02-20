# Module for user handling

# pylint: disable=E1101

from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash


# Function for user login
# If user gives correct username and password, then user's id is
# set to session which means the user is logged in


def login(username, password):

    sql = "SELECT password, id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if user == None:
        return False
    else:
        if check_password_hash(user[0], password):
            session["user_id"] = user[1]
            return True
        else:
            return False

# Function for user logout
# user_id is removed from session which means the user is
# then logged out


def logout():
    del session["user_id"]

# Function for registering user
# If adding user information to users table is successfull then user
# is logged in


def register(username, password):
    hash_value = generate_password_hash(password)
    admin = False
    try:
        sql = "INSERT INTO users (username, password, admin) VALUES (:username, :password, :admin)"
        db.session.execute(
            sql, {"username": username, "password": hash_value, "admin": admin})
        db.session.commit()
    except:
        return False
    return login(username, password)

# Function for checking if user is logged in
# Returns user id if user is logged in, otherwise 0


def user_id():
    return session.get("user_id", 0)

def get_admin_status():
    user_id = session.get("user_id", 0)
    try:
        sql = "SELECT admin FROM users WHERE id=:user_id"
        result = db.session.execute(sql, {"user_id":user_id})
        admin = result.fetchone()
    except:
        return False
    return admin[0]