from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

from flask.helpers import flash

app = Flask(__name__)
app.secret_key = "sandhuz"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("index.html", login = login)

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True # remain in session even if we close browser
        user = request.form["nm"]
        session["user"] = user
        flash("Login Successful")
        return redirect(url_for("user"))
    else:
        if "user" in session: # if user is in session no need to login
            flash("Already Logged In")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user = user)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    flash("Logged Out", "info")
    # flash(f"Logged Out, {user}", "info")
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run()
