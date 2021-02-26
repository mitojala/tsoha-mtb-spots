# Module for handling page requests

from app import app
from flask import render_template, request, redirect, jsonify
import users
import spots
import json
import simplejson
import base64
import io
from os import getenv
from json import JSONEncoder
from sqlalchemy_serializer import SerializerMixin

class MyEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__ 

# Function returning main page

@app.route("/")
def index():
    return render_template("index.html")

# Function returning mtb spots main page containing a list of
# mtb spots.


def without_keys(d, keys):
    return {key: d[key] for key in d if key not in keys}

def get_json_spot_list(spot_list):

    # Chance spot list format to JSON in order to use these in spots_main to create
    # Google Maps markers

    # _sa_instance_state and datetime are not JSON serializable
    invalid = {"_sa_instance_state", "sent_at"}  
    # Create a dictionary list for simplejson.dumps()
    dict_list = []
    for spot in spot_list:
        spot_dict = spot.__dict__
        spot_dict_without_invalid = without_keys(spot_dict, invalid)
        dict_list.append(spot_dict_without_invalid)
    return simplejson.dumps(dict_list)

@app.route("/spots_main", methods=["GET", "POST"])
def spots_main():

    # Check if user has admin privileges
    admin = users.get_admin_status()

    if request.method == "GET":
        spot_list = spots.get_spot_list()
        spotsJson = get_json_spot_list(spot_list)
        return render_template("spots_main.html", spots=spot_list, spotsJson=spotsJson, admin=admin)
    if request.method == "POST":
        spot_id = request.form["spot_id"]
        spots.remove_spot(spot_id)
        spot_list = spots.get_spot_list()
        spotsJson = get_json_spot_list(spot_list)
        return render_template("spots_main.html", spots=spot_list, spotsJson=spotsJson, admin=admin)

@app.route("/show_spot_image/<int:id>")
def show_image(id):
    return render_template("show_spot_image.html", id=id)

@app.route("/spot_image/<int:id>")
def get_image(id):
    image = spots.show(id)
    return image

# Function returning page for adding new mtb spots

@app.route("/add_spot", methods=["GET", "POST"])
def add_spot():
    if request.method == "GET":
        google_maps_url = getenv("GOOGLE_MAPS_URL")
        return render_template("add_spot.html", google_maps_url=google_maps_url)
    if request.method == "POST":
        name = request.form["name"]
        spot_type = request.form["spot_type"]
        description = request.form["description"]
        difficulty = request.form["difficulty"]
        latitude = request.form["lat"]
        longitude = request.form["long"]
        file = request.files["file"]
        spot_image = file.read()
        visible = True
        if len(spot_image) == 0:
            if spots.add_spot(name, spot_type, description, difficulty, latitude, longitude, visible):
                return redirect("/spots_main")
            else:
                return render_template("error.html", message="Spottin lisäyksessä ilmeni virhe")
        else:
            if spots.add_spot_with_image(name, spot_type, description, difficulty, latitude, longitude, visible, spot_image):
                return redirect("/spots_main")
            else:
                return render_template("error.html", message="Spottin lisäyksessä ilmeni virhe")
# User login
# If method is GET then login page is shown
# If method is POST then the login form is handled and user is
# redirected to main page if valid username and pasword are given,
# otherwise redirect to error page


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Väärä käyttäjätunnus tai salasana")


# User logout
# Done with function logout from module users

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

# User registering
# If method is GET user registering page is shown
# If method is POST then the registering form is handled and
# if successfull then user is redirected to main page
# otherwise redirect to error page


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not len(username) >= 4:
            return render_template("error.html", message="Käyttäjänimen pitää olla vähintään neljä (4) merkkiä pitkä.")
        if not len(password) >= 6:
            return render_template("error.html", message="Salasanan pitää olla vähintään kuusi (6) merkkiä pitkä.")
        if users.register(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Virhe käyttäjätilin luomisessa, yritä uudelleen")
