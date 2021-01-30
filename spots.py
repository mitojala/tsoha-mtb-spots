from db import db
import users


def get_spot_list():
    sql = "SELECT * FROM spots"
    result = db.session.execute(sql)
    return result.fetchall()
