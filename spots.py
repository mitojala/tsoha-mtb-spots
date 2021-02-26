# Module for mtb spot handling

# pylint: disable=E1101

from db import db
from sqlalchemy_serializer import SerializerMixin
import users
from flask import make_response

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
    has_image = db.Column(db.Boolean)
    visible = db.Column(db.Boolean)

    def __init__(self, name, spot_type, description, difficulty, latitude, longitude, sent_at, has_image, visible):
        self.name = name
        self.spot_type = spot_type
        self.description = description
        self.difficulty = difficulty
        self.latitude = latitude
        self.longitude = longitude
        self.sent_at = sent_at
        self.has_image = has_image
        self.visible = visible

# Function returning all mtb spots

def get_spot_list():
    # sql = "SELECT * FROM spots"
    # result = db.session.execute(sql)
    # return result.fetchall()
    return Spots.query.filter_by(visible=True).all()

# Function returning all mtb spots images

def get_spot_image_list():
    sql = "SELECT * FROM spot_images"
    result = db.session.execute(sql)
    return result.fetchall()

# Function for inserting a new mtb spot WITHOUT image into database

def add_spot(name, spot_type, description, difficulty, latitude, longitude, visible):
    user_id = users.user_id()
    if user_id == 0:
        return False

    try:
        sql = "INSERT INTO spots (name,spot_type,description,difficulty,latitude,longitude,sent_at,has_image,visible) VALUES (:name,:spot_type,:description,:difficulty,:latitude,:longitude,NOW(),FALSE,:visible)"
        db.session.execute(sql, {"name": name, "spot_type": spot_type, "description": description, "difficulty": difficulty, "latitude": latitude, "longitude": longitude, "has_image": False, "visible": visible})
        db.session.commit()
    except:
        return False
    return True

# Function for inserting a new mtb spot WITH image into database

def add_spot_with_image(name, spot_type, description, difficulty, latitude, longitude, visible, spot_image):
    user_id = users.user_id()
    if user_id == 0:
        return False

    try:
        sql = "INSERT INTO spots (name,spot_type,description,difficulty,latitude,longitude,sent_at,has_image,visible) VALUES (:name,:spot_type,:description,:difficulty,:latitude,:longitude,NOW(),TRUE,:visible) RETURNING id"
        result = db.session.execute(
        sql, {"name": name, "spot_type": spot_type, "description": description, "difficulty": difficulty, "latitude": latitude, "longitude": longitude, "has_image": True, "visible": visible})
        spot_id = result.fetchone()[0]
        sql = "INSERT INTO spot_images (spot_id, spot_image) VALUES (:spot_id, :spot_image)"
        db.session.execute(sql, {"spot_id":spot_id, "spot_image":spot_image})
        db.session.commit()
    except:
        return False
    return True

# TODO
# Function for inserting an image to existing spot

# def add_image_to_spot(spot_id, image):
    

# Function for removing a spot from list
# The spot is not deleted from database but rather set not to be visible

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

# Function for showing spot image

def show(spot_id):
    sql = "SELECT spot_image FROM spot_images WHERE spot_id=:spot_id"
    result = db.session.execute(sql, {"spot_id":spot_id})
    data = result.fetchone()[0]
    response = make_response(bytes(data))
    response.headers.set("Content-Type","image/jpeg")
    return response