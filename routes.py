# Module for handling page requests

from app import app
from flask import render_template, request, redirect
import users
import spots
from os import getenv

# Function returning main page


@app.route("/")
def index():
    return render_template("index.html")

# Function returning mtb spots main page containing a list of
# mtb spots.


@app.route("/spots_main")
def spots_main():
    list = spots.get_spot_list()
    return render_template("spots_main.html", spots=list)

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
        if spots.add_spot(name, spot_type, description):
            return redirect("/spots_main")
        else:
            return render_template("error.html", message="Spottin lisäyksessä ilmeni virhe")

# Function returning main page


@app.route("/add_spot_to_map")
def add_spot_to_map():
    return render_template("add_spot_to_map.html")

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
