from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task

@app.route("/")
def home():
    # Sets homepage for the site when it's loaded #
    return render_template("tasks.html")