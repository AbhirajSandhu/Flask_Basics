# create __init__.py in admin dir to make static templates and other work

from flask import Flask, render_template
# from second import second   # if in same folder
from admin.second import second

app = Flask(__name__)
app.register_blueprint(second, url_prefix="/admin")

@app.route("/")
def test():
    return "<h1>Test</h1>"

if __name__ == "__main__":
    app.run(debug=True)
