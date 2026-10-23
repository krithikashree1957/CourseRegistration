
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary in-memory course list
courses = []
next_id = 1


@app.route("/")
def home():
    return render_template("index.html", courses=courses)


@app.route("/add", methods=["POST"])
def add_course():
    global next_id

    course_name = request.form.get("course_name", "").strip()
    course_code = request.form.get("course_code", "").strip()

    if course_name and course_code:
        courses.append({
            "id": next_id,
            "name": course_name,
            "code": course_code
        })
        next_id += 1

    return redirect(url_for("home"))


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
