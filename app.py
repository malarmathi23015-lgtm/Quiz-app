from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "quiz_secret_key_123"

questions = [
    {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
    {"question": "What is 12 x 12?", "options": ["124", "144", "132", "148"], "answer": "144"},
    {"question": "Who invented the telephone?", "options": ["Thomas Edison", "Nikola Tesla", "Alexander Graham Bell", "Albert Einstein"], "answer": "Alexander Graham Bell"},
    {"question": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific"}
]

@app.route("/")
def index():
    session.clear()
    return render_template("index.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if "current" not in session:
        session["current"] = 0
        session["score"] = 0
        session["answers"] = []
    if request.method == "POST":
        selected = request.form.get("answer")
        current = session["current"]
        correct = questions[current]["answer"]
        if selected == correct:
            session["score"] += 1
        session["answers"] = session.get("answers", []) + [{"question": questions[current]["question"], "selected": selected, "correct": correct}]
        session["current"] = current + 1
        if session["current"] >= len(questions):
            return redirect(url_for("result"))
    current = session["current"]
    if current >= len(questions):
        return redirect(url_for("result"))
    q = questions[current]
    return render_template("quiz.html", question=q, number=current + 1, total=len(questions))

@app.route("/result")
def result():
    score = session.get("score", 0)
    total = len(questions)
    answers = session.get("answers", [])
    return render_template("result.html", score=score, total=total, answers=answers)

if __name__ == "__main__":
    app.run(debug=True)
