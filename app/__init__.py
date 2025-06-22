import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from .data import work_experiences  # Import work experiences from data.py

load_dotenv()
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
