from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Question database
questions_db = {
    "data": [
        "What is SQL?",
        "Explain Pandas",
        "What is data cleaning?"
    ],
    "web": [
        "What is HTML?",
        "Explain CSS",
        "What is JavaScript?"
    ],
    "software": [
        "What is OOP?",
        "Explain inheritance",
        "What is a class?"
    ]
}

# Keywords for evaluation
keywords = {
    "sql": ["database", "query", "table"],
    "pandas": ["dataframe", "analysis"],
    "html": ["structure", "web"],
    "oop": ["object", "class"]
}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        role = request.form["role"]
        questions = questions_db.get(role, [])
        return render_template("interview.html", questions=questions, role=role)
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    answers = request.form.to_dict()
    score = 0
    feedback = []

    for key, answer in answers.items():
        answer = answer.lower()
        matched = False

        for word, keys in keywords.items():
            if word in key:
                if any(k in answer for k in keys):
                    score += 10
                    feedback.append(f"{key}: Good answer")
                    matched = True
                    break

        if not matched:
            feedback.append(f"{key}: Improve your answer")

    return render_template("result.html", score=score, feedback=feedback)

if __name__ == "__main__":
    app.run(debug=True)