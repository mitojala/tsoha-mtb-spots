# Module for mtb spot handling

# pylint: disable=E1101

from db import db
from sqlalchemy_serializer import SerializerMixin
import users

class Spots(db.Model, SerializerMixin):

    __tablename__ = 'spots'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    spot_type = db.Column(db.Text)
    description = db.Column(db.Text)
    latitude = db.Column(db.Numeric)
    longitude = db.Column(db.Numeric)
    sent_at = db.Column(db.DateTime)

    def __init__(self, name, spot_type, description, latitude, longitude, sent_at):
        self.name = name
        self.spot_type = spot_type
        self.description = description
        self.latitude = latitude
        self.longitude = longitude
        self.sent_at = sent_at

# Function returning all mtb spots


def get_spot_list():
    # sql = "SELECT * FROM spots"
    # result = db.session.execute(sql)
    # return result.fetchall()
    return Spots.query.all()

# Function for inserting a new mtb spot into database

def add_spot(name, spot_type, description, latitude, longitude):
    user_id = users.user_id()
    if user_id == 0:
        return False

    print(name, spot_type, description)
    # try:
    sql = "INSERT INTO spots (name,spot_type,description, latitude, longitude, sent_at) VALUES (:name,:spot_type,:description,:latitude,:longitude,NOW())"
    db.session.execute(
        sql, {"name": name, "spot_type": spot_type, "description": description, "latitude": latitude, "longitude": longitude})
    db.session.commit()
    # except:
    #     return False
    return True
