work_experiences = [
    {
        "role": "Production Engineering Fellow",
        "company": "Meta x MLH",
        "dates": "Summer 2025",
        "location": "Remote USA",
        "responsibilities": []
    },
    {
        "role": "Undergraduate Research Assistant",
        "company": "Washington State University",
        "dates": "2023–2024",
        "location": "Pullman, Washington USA",
        "responsibilities": [
            "Analyzed security vulnerabilities in LLM-generated code and applied Bayesian optimization to enhance prompt accuracy for secure and functionally correct code generation."
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
            "Optimized internal database processes with C++ and SQL, reducing runtime by 66%.",
            "Enhanced data visualization through real-time dashboards and dynamic graphs."
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

hobbies = [
    {
        "name": "Watching TV Shows",
        "image": "img/hobbies/watching_tv.jpg",
        "description": "I’m currently binge-watching Community (Troy and Abed are my favorites!) and plan to finish Suits soon."
    },
    {
        "name": "Learning Guitar",
        "image": "img/hobbies/learning_guitar.jpg",
        "description": "I’m teaching myself guitar—it’s a fun challenge, but my fingernails are always short!"
    },
    {
        "name": "Playing Volleyball",
        "image": "img/hobbies/playing_volleyball.jpg",
        "description": "I play both indoor and beach volleyball to stay active and have fun."
    }
]

education = [
    {
        "school": "Washington State University, Honors College",
        "years": "2021–2025",
        "degree": "B.S. in Computer Science, Minor in Mathematics (Summa Cum Laude)",
        "location": "Pullman, Washington USA",
        "gpa": "GPA 3.94",
        "details": [
            "Graduated with honors, focusing on AI, machine learning, and mathematics.",
            "Capstone Project: Retrieval-Augmented Generation (RAG) using Knowledge Graphs and Vector Search",
            "Honors College",
            "NIH MARC Fellow",
            "ESTEEMED MIRA Scholar",
            "VCEA College Ambassador"
        ]
    }
]

places = [
    {"city": "Pullman, WA", "coords": [46.7298, -117.1817]},
    {"city": "Pittsburgh, PA", "coords": [40.4406, -79.9959]},
    {"city": "Sunnyvale, CA", "coords": [37.3688, -122.0363]},
    {"city": "Corvallis, OR", "coords": [44.5646, -123.2620]}
]

news_items = [
    {
        "date": "06/2025",
        "content": 'Gave an alumni talk for the <a href="https://marc.wsu.edu/" class="text-primary underline">WSU MARC</a> & <a href="https://mira.wsu.edu/" class="text-primary underline">MIRA</a> program on my research journey and grad school advice.',
    },
    {
        "date": "06/2025",
        "content": 'I joined the <a href="https://fellowship.mlh.io/programs/production-engineering-sre" class="text-primary underline">Meta x MLH Fellowship</a> as a Production Engineering Fellow!',
    },
    {
        "date": "05/2025",
        "content": "Graduated from Washington State University with a B.S. in Computer Science and a minor in Mathematics. Go Cougs!",
    },
    {
        "date": "06/2024",
        "content": 'This summer, I will be conducting research at Carnegie Mellon University as part of the <a href="https://riss.ri.cmu.edu/" class="text-primary underline">CMU RISS</a> program.',
    },
    {
        "date": "09/2023",
        "content": 'I will be participating in Google Research\'s <a href="https://research.google/programs-and-events/csrmp/" class="text-primary underline">CS Research Mentorship Program</a> during the Fall semester.',
    },
    {
        "date": "07/2023",
        "content": 'I am thrilled and sincerely grateful to have been awarded the <a href="https://buildyourfuture.withgoogle.com/scholarships/generation-google-scholarship" class="text-primary underline">Generation Google Scholarship</a>.',
    },
    # Hidden news items
    {
        "date": "07/2023",
        "content": "My contributions to the work I completed at Oregon State University have been accepted for presentation at <b>IROS 2023</b>!",
        "hidden": True,
    },
    {
        "date": "05/2023",
        "content": 'I will be interning as a <a href="https://buildyourfuture.withgoogle.com/programs/step" class="text-primary underline">STEP Intern</a> at Google.',
        "hidden": True,
    },
    {
        "date": "05/2023",
        "content": 'I became a MARC Scholar through the <a href="https://marc.wsu.edu/" class="text-primary underline">NIH Fellowship</a>.',
        "hidden": True,
    },
    {
        "date": "06/2022",
        "content": 'I will be conducting research at Oregon State University as part of the <a href="https://engineering.oregonstate.edu/CoRIS/reu-robots-real-world" class="text-primary underline">REU: Robots in the Real World</a> program.',
        "hidden": True,
    },
    {
        "date": "07/2021",
        "content": 'I became an ESTEEMED Scholar through the <a href="https://mira.wsu.edu/" class="text-primary underline">NIH Fellowship</a>.',
        "hidden": True,
    },
]

research_papers = [
    {
        "title": "Social Triangles and Aggressive Lines: Multi-Robot Formations Impact Navigation and Approach",
        "authors": [
            "Alexandra Bacula",
            "Ethan Villalovoz",
            "Deanna Flynn",
            "Ankur Mehta",
            "Heather Knight",
        ],
        "conference": "IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 2023",
        "pdf": "/static/data/research/2023_IROS_Social_Triangles_Agressive_Lines_bacula.pdf",
        "bibtex": "/static/data/research/2023_IROS_Social_Triangles_Agressive_Lines_bacula.bib",
        "image": "/static/data/research/STAL_Multi_Robot_Formations.jpeg",
        "description": "Investigates how different multi-robot formations affect navigation and approach behaviors in social environments. Demonstrates the impact of formation geometry on human-robot interaction and navigation efficiency.",
        "tags": ["Robotics", "Multi-Robot", "Human-Robot Interaction"],
    },
    # Add more papers as needed
]
