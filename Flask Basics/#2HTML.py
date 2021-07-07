from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("index.html", content = name)

if __name__ == "__main__":
    app.run()


    # <h1>Home Page</h1>
    # <p>{{content}}</p>
    # {% for x in range(10)%}
    #     {% if x % 2 == 0 %}
    #     <p>{{x}} Raja the King</p>
    #     {% endif %}
    # {% endfor %}

    # if content = ["raja", "the", "king"]
    # {% for x in content%}
    #     <p>{{x}}</p>
    # {% endfor %}