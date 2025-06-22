from flask import Flask, render_template
import os
from .data import work_experiences, hobbies  # Import hobbies

app = Flask(__name__)


@app.route("/")
def index():
    user = {"name": "Ethan Villalovoz"}
    return render_template(
        'index.html',
        title="MLH Fellow",
        url=os.getenv("URL"),
        user=user,
        work_experiences=work_experiences
    )


@app.route("/hobbies")
def hobbies_page():
    user = {"name": "Ethan Villalovoz"}
    return render_template(
        'hobbies.html',
        title="My Hobbies",
        url=os.getenv("URL"),
        user=user,
        hobbies=hobbies
    )
