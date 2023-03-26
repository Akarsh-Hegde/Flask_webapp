from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from . import db
from passlib.hash import pbkdf2_sha256
import uuid

auth = Blueprint('auth', __name__)

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        user = {
        "_id": uuid.uuid4().hex,
        "name": request.form.get('name'),
        "email": request.form.get('email'),
        "password1": request.form.get('password1'),
        "password2": request.form.get('password2'),
        }
        if db.user.find_one({"email": user['email']}) is not None:
            flash("Email already exists", category="error")
        elif user['password1'] != user['password2']:
            flash("password dont match", category="error")
        elif len(user['password1']) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            print(user['name'])
            user['password1'] = pbkdf2_sha256.encrypt(user['password1'])
            db.user.update_one({"email": user['email']},{"$unset": {"password2": ""}})
            user1 = db.user  # get the user collection in mongobd db
            user1.insert_one(user)

            flash('Account created!', category='success')
            return redirect(url_for("auth.login"))

    return render_template("sign_up.html")


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user_login = db.user.find_one({"email": email}) 
        if user_login:
            if pbkdf2_sha256.verify(password, user_login['password1']):
                flash("Logged in successfully!", category='success')
                session["_id"] = user_login["_id"]
                # print(session["_id"])

                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password, try again", category="error")
        else:
            flash("email does not exist", category="error")
        
    return render_template("login.html")


@auth.route("/logout")
def logout():
    session.pop("_id", None)
    return redirect(url_for("auth.login"))
