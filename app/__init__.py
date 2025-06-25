from flask import Flask, render_template, request
import os
from .data import work_experiences, hobbies, education, places  # Import education and places
from .data import news_items

app = Flask(__name__)


@app.route("/")
def index():
    show_all_news = request.args.get("show_all_news", "false") == "true"
    visible_news = [item for item in news_items if not item.get("hidden")]
    hidden_news = [item for item in news_items if item.get("hidden")]
    news = visible_news + (hidden_news if show_all_news else [])
    user = {"name": "Ethan Villalovoz"}
    return render_template(
        'index.html',
        title="MLH Fellow",
        url=os.getenv("URL"),
        user=user,
        work_experiences=work_experiences,
        hobbies=hobbies,
        education=education,
        places=places,
        news=news,
        show_all_news=show_all_news,
        hidden_news=hidden_news,
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


@app.route("/research")
def research_page():
    return render_template("research.html")


@app.route("/projects")
def projects_page():
    return render_template("projects.html")


@app.route("/teaching")
def teaching_page():
    return render_template("teaching.html")


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


@app.route("/places")
def places_page():
    return render_template("places.html")
