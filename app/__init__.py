import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route("/")
def index():
    user = {"name": "Ethan Villalovoz"}
    work_experiences = [
        {
            "role": "Production Engineering Fellow",
            "company": "Meta x MLH",
            "dates": "Summer 2025",
            "location": "Remote USA",
            "responsibilities": [
                "Selected for the Meta x MLH Production Engineering Fellowship (acceptance rate < 2.5%), a 12-week program focused on Site Reliability Engineering (SRE), DevOps, and large-scale infrastructure."
            ]
        },
        {
            "role": "Robotics Institute Summer Scholar",
            "company": "Carnegie Mellon University",
            "dates": "Summer 2024",
            "location": "Pittsburgh, Pennsylvania USA",
            "responsibilities": [
                "Developed hierarchical reward learning systems leveraging Bayesian inference and human feedback to align autonomous systems with human preferences and improve adaptability in dynamic settings."
            ]
        },
        {
            "role": "STEP Intern",
            "company": "Google",
            "dates": "Summer 2023",
            "location": "Sunnyvale, California USA",
            "responsibilities": [
                "Optimized internal database processes with C++ and SQL, reducing runtime by 66% and enhancing data visualization through real-time dashboards and dynamic graphs."
            ]
        },
        {
            "role": "Robots in the Real World Researcher",
            "company": "Oregon State University",
            "dates": "Summer 2022",
            "location": "Corvallis, Oregon USA",
            "responsibilities": [
                "Developed geometric features for multi-robot expressive motion, integrating performing arts techniques to enhance robot character and intelligence."
            ]
        }
    ]
    return render_template(
        'index.html',
        title="MLH Fellow",
        url=os.getenv("URL"),
        user=user,
        work_experiences=work_experiences
    )
