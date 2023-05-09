from flask_app import app
from flask import render_template, redirect, request, url_for, session
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models import user

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if not user.User.is_valid(request.form):
        return redirect(url_for("index"))
    else:
        data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"],
            "password": bcrypt.generate_password_hash(request.form["password"])
        }
        user.User.create(data)
        session["first_name"] = data["first_name"]
        session["last_name"] = data["last_name"]
        session["email"] = data["email"]
        session["password"] = data["password"]

    return "Success"

@app.route("/login", methods=["POST"])
def login():
    if not user.User.valid_login(request.form):
        return redirect(url_for("index"))
    else:
        data = {
            "email": request.form["email"],
            "password": bcrypt.generate_password_hash(request.form["password"])
        }
        user.User.create(data)
    return redirect(url_for("index")) 