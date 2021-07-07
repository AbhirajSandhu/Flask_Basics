# TEMPLATE INHERITENCE

from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()


# <!DOCTYPE html>
# <html>
# <head>
#     <title>{% block title %}{% endblock %}</title>
# </head>
# <body>
#     <h1>SandhuZ</h1>
#     {% block content %}
#     {% endblock %}
# </body>
# </html>

# {% extends "base.html" %}
# {% block title %}Home Page{% endblock %}

# {% block content %}
# {% endblock %}
