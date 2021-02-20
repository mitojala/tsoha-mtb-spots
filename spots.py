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
    difficulty = db.Column(db.Numeric)
    latitude = db.Column(db.Numeric)
    longitude = db.Column(db.Numeric)
    sent_at = db.Column(db.DateTime)
    visible = db.Column(db.Integer)

    def __init__(self, name, spot_type, description, difficulty, latitude, longitude, sent_at, visible):
        self.name = name
        self.spot_type = spot_type
        self.description = description
        self.difficulty = difficulty
        self.latitude = latitude
        self.longitude = longitude
        self.sent_at = sent_at
        self.visible = visible

# Function returning all mtb spots


def get_spot_list():
    # sql = "SELECT * FROM spots"
    # result = db.session.execute(sql)
    # return result.fetchall()
    return Spots.query.filter_by(visible=True).all()

# Function for inserting a new mtb spot into database

def add_spot(name, spot_type, description, difficulty, latitude, longitude, visible):
    user_id = users.user_id()
    if user_id == 0:
        return False

    try:
        sql = "INSERT INTO spots (name,spot_type,description,difficulty,latitude,longitude,sent_at, visible) VALUES (:name,:spot_type,:description,:difficulty,:latitude,:longitude,NOW(),:visible)"
        db.session.execute(
        sql, {"name": name, "spot_type": spot_type, "description": description, "difficulty": difficulty, "latitude": latitude, "longitude": longitude, "visible": visible})
        db.session.commit()
    except:
        return False
    return True

def remove_spot(spot_id):
    user_id = users.user_id()
    if user_id == 0:
        return False

    try:
        sql = "UPDATE spots SET visible=False WHERE id=:id"
        db.session.execute(
        sql, {"id": spot_id})
        db.session.commit()
    except:
        return False
    return True