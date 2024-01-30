from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task

@app.route("/")
def home():
    # Sets homepage for the site when it's loaded #
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


"""
When a user clicks the "Add Category" button, this will use the "GET" method and render the 'add_category' template.
Once they submit the form, this will call the same function, but will check if the request
being made is a “POST“ method, which posts data somewhere, such as a database.
Anything that needs to be handled by the POST method, should be indented properly within this condition.
By default, the normal method is GET, so it will behave as the 'else' condition since
it's not part of the indented POST block.
"""


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")