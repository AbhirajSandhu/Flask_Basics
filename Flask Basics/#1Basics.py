from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello <h1>Abhiraj</h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}"
# f for returning strings

# redirect back to home
from flask import redirect
from flask.helpers import url_for
@app.route("/admin")
def admin():
    return redirect(url_for("home"))
   # return redirect(url_for("user", name = "Admin"))

if __name__ == "__main__":
    app.run()
