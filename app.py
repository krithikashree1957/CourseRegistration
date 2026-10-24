
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

courses = [
    {"id": 1, "name": "Python Programming"},
    {"id": 2, "name": "Web Development"},
    {"id": 3, "name": "Database Systems"}
]

registrations = []
next_registration_id = 1


@app.route("/")
def home():
    return render_template(
        "index.html",
        courses=courses,
        registrations=registrations
    )


@app.route("/add", methods=["POST"])
def add_course():
    course_name = request.form.get("course_name", "").strip()

    if course_name:
        courses.append({
            "id": len(courses) + 1,
            "name": course_name
        })

    return redirect(url_for("home"))


@app.route("/register", methods=["POST"])
def register_student():
    global next_registration_id

    student_name = request.form.get("student_name", "").strip()
    course_id = request.form.get("course_id", "").strip()

    if not student_name or not course_id:
        return "Student name and course are required.", 400

    course = next(
        (c for c in courses if str(c["id"]) == course_id),
        None
    )

    if course is None:
        return "Course not found.", 404

    registrations.append({
        "id": next_registration_id,
        "student_name": student_name,
        "course_id": course["id"],
        "course_name": course["name"]
    })

    next_registration_id += 1

    return redirect(url_for("home"))

@app.route("/registrations")
def view_registrations():
    return render_template(
        "registrations.html",
        registrations=registrations
    )

@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
