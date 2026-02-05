from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # User Data (Pre-filled based on your profile)
    user_info = {
        "name": "Atharva Sanjay Dharankar",
        "role": "Engineering Student & Developer",
        "location": "Rampur, Nashik, Maharashtra, India",
        "coordinates": "19°53'27.8N 74°16'02.6E", 
        "bio_headline": "Building Python automation tools and Electromechanical systems.",
        "about_text": "I am passionate about robotics, photography, and coding. I specialize in building autonomous systems and useful Python utilities.",
    }

    # Projects (Pre-filled with your known projects)
    projects = [
        {
            "id": "01",
            "title": "Autonomous Water Surface Cleaning Robot",
            "category": "Robotics",
            "description": "A robot designed to autonomously navigate and clean water surfaces using Arduino control systems.",
            "tech_stack": ["Arduino", "C++","Path finding Algorithm", "Motors","Ultrasonic Sensors"]
        },
        {
            "id": "02",
            "title": "Smart Stick for Visually Impaired",
            "category": "Assistive Tech",
            "description": "An intelligent walking stick equipped with ultrasonic sensors to detect obstacles and alert the user.",
            "tech_stack": ["Arduino", "Ultrasonic Sensors","Vibration motors", "Embedded Systems"]
        },
        {
            "id": "03",
            "title": "Web Activity Tracker",
            "category": "Python Automation",
            "description": "A Python-based tool that tracks time spent on websites and issues warnings to improve productivity.",
            "tech_stack": ["Python", "Automation", "Data Logging","Web tracking"]
        }
        ]

    # Skills (Pre-filled)
    skills = [
        "Python", "Arduino", "Electromechanics", 
        "Photography", "Sensors", "Circuit Design", 
        "And Loading more skills...",
        ]

    return render_template('index.html', user=user_info, projects=projects, skills=skills)

app.run()