
from app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Course Registration System - V2" in response.data


def test_add_course():
    client = app.test_client()
    response = client.post(
        "/add",
        data={"course_name": "Cloud Computing"}
    )
    assert response.status_code == 302


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_student_registration():
    client = app.test_client()
    response = client.post(
        "/register",
        data={"student_name": "Test Student", "course_id": "1"}
    )
    assert response.status_code == 302
def test_view_registrations():
    response = app.test_client().get("/registrations")
    assert response.status_code == 200
    assert b"All Student Registrations" in response.data