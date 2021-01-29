# Module for handling page requests

from app import app
from flask import render_template, request, redirect
import users


# Function returning main page

@app.route("/")
def index():
    return render_template("index.html")

# Function returning mtb spots main page


@app.route("/spots_main")
def spots_main():
    return render_template("spots_main.html")

# User login
# If method is GET then login page is shown
# If method is POST then the login form is handled and user is
# redirected to main page if valid username and pasword are given,
# otherwise redirect to error page


@app.route("/login", methods=["get", "post"])
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


@app.route("/register", methods=["get", "post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Virhe käyttäjätilin luomisessa, yritä uudelleen")
