# Module for mtb spot handling

# pylint: disable=E1101

from db import db
import users

# Function returning all mtb spots


def get_spot_list():
    sql = "SELECT * FROM spots"
    result = db.session.execute(sql)
    return result.fetchall()


# Function for inserting a new mtb spot into database

def add_spot(name, spot_type, description):
    user_id = users.user_id()
    if user_id == 0:
        return False
    print(name, spot_type, description)
    try:
        sql = "INSERT INTO spots (name,type,description,sent_at) VALUES (:name,:spot_type,:description, NOW())"
        db.session.execute(
            sql, {"name": name, "spot_type": spot_type, "description": description})
        db.session.commit()
    except:
        return False
    return True
