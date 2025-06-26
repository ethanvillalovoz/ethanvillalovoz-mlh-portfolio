from flask import Flask, render_template, request, redirect, flash, url_for
import os
from .data import work_experiences, hobbies, education, places  # Import education and places
from .data import news_items, research_papers, projects, teaching_experiences  # Add teaching_experiences import
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    show_all_news = request.args.get("show_all_news", "false") == "true"
    # Always pass all news items to the template
    news = news_items
    hidden_news = [item for item in news_items if item.get("hidden")]
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
    return render_template('research.html', research_papers=research_papers, current_year=datetime.now().year, title="Research")


@app.route("/projects")
def projects_page():
    return render_template("projects.html", projects=projects, current_year=datetime.now().year, title="Projects")


@app.route("/teaching")
def teaching_page():
    return render_template("teaching.html", teaching_experiences=teaching_experiences, current_year=datetime.now().year, title="Teaching")


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        if not name or not email or not message:
            flash("All fields are required.", "error")
            return redirect(url_for("index") + "#contactForm")
        # Here you would handle sending the message (e.g., email, save to DB, etc.)
        flash("Thank you for reaching out! Your message has been sent.", "success")
        return redirect(url_for("index") + "#contactForm")
    return render_template("contact.html")


from app.data import places

@app.route('/places')
def places_page():
    return render_template("places.html", places=places, title="Places", current_year=2025)
