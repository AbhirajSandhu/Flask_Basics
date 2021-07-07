from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

from flask.helpers import flash

app = Flask(__name__)
app.secret_key = "sandhuz"
app.permanent_session_lifetime = timedelta(minutes=5)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3' # users is table name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class users(db.Model):
    _id   = db.Column("id"   , db.Integer , primary_key=True)
    name  = db.Column("name" , db.String(100))
    email = db.Column("email", db.String(100))

    def __init__(self, name, email):
        self.name  = name
        self.email = email

@app.route("/")
def home():
    return render_template("index.html", login = login)

@app.route("/view")
def view():
    return render_template("view.html", values = users.query.all())

@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email   # store email in session
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("Email was saved")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", user = user)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True # remain in session even if we close browser
        user = request.form["nm"]
        session["user"] = user

        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user, "")
            db.session.add(usr)  # save current model in session to db
            db.session.commit()         # necessary to commit for permanent changes

        flash("Login Successful")
        return redirect(url_for("user"))
    else:
        if "user" in session: # if user is in session no need to login
            flash("Already Logged In")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/logout")
def logout():
    flash("Logged Out", "info")
    # flash(f"Logged Out, {user}", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    db.create_all()   # should run before app
    app.run(debug=True)
