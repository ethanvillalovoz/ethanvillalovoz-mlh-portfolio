from flask import Flask, render_template, request, redirect, flash, url_for, jsonify
import os, time, re
from .data import work_experiences, hobbies, education, places
from .data import news_items, research_papers, projects, teaching_experiences
from datetime import datetime
from peewee import *
from playhouse.shortcuts import model_to_dict
from dotenv import load_dotenv

# (Keep mysql-connector imports if used elsewhere)
import mysql.connector
from mysql.connector import Error

load_dotenv()

app = Flask(__name__)

EMAIL_REGEX = re.compile(r"^[^@]+@[^@]+\.[^@]+$")

# --- Database config ---
if os.getenv("TESTING") == "true":
    print("Running in test mode (SQLite)")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    MYSQL_HOST = os.getenv("MYSQL_HOST", "mysql")   # MUST be "mysql" in docker
    MYSQL_DB   = os.getenv("MYSQL_DATABASE", "myportfoliodb")
    MYSQL_USER = os.getenv("MYSQL_USER", "myportfolio")
    MYSQL_PASS = os.getenv("MYSQL_PASSWORD", "mypassword")

    mydb = MySQLDatabase(
        MYSQL_DB,
        user=MYSQL_USER,
        password=MYSQL_PASS,
        host=MYSQL_HOST,
        port=3306
    )

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = mydb

# --- Connect with a brief retry to avoid race with DB startup ---
if os.getenv("TESTING") == "true":
    mydb.connect(reuse_if_open=True)
else:
    for attempt in range(30):  # up to ~60s (30 x 2s)
        try:
            mydb.connect(reuse_if_open=True)
            break
        except OperationalError as e:
            print(f"DB not ready (attempt {attempt+1}/30): {e}")
            time.sleep(2)

# Ensure table exists
mydb.create_tables([TimelinePost])

# --- Health endpoint that touches the DB ---
@app.route("/health")
def health_check():
    try:
        if os.getenv("TESTING") == "true":
            cursor = mydb.execute_sql("SELECT datetime('now')")
        else:
            cursor = mydb.execute_sql("SELECT NOW()")
        result = cursor.fetchone()
        db_time = result[0] if result else None
        return jsonify({"status": "ok", "time": str(db_time)}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

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

@app.route('/timeline')
def timeline():
    return render_template("timeline.html", title="Timeline")

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form.get('name')
    email = request.form.get('email')
    content = request.form.get('content')

    if not name or name.strip() == "":
        return "Invalid name", 400

    if not email or not EMAIL_REGEX.match(email):
        return "Invalid email", 400

    if not content or content.strip() == "":
        return "Invalid content", 400

    timeline_post = TimelinePost.create(
        name=name,
        email=email,
        content=content
    )

    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        "timeline_posts": [
            model_to_dict(post) 
            for post in 
    TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/api/timeline_post/<int:post_id>', methods=['DELETE'])
def delete_time_line_post(post_id):
    try:
        post = TimelinePost.get(TimelinePost.id == post_id)
        post.delete_instance()
        return {"status": "success", "message": "Post deleted successfully."}, 200
    except TimelinePost.DoesNotExist:
        return {"status": "error", "message": "Post not found."}, 404