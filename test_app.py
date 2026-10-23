
import pytest
from app import app, courses


@pytest.fixture(autouse=True)
def reset_courses():
    courses.clear()
    yield
    courses.clear()


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Add Courses" in response.data


def test_add_course():
    client = app.test_client()

    response = client.post(
        "/add",
        data={
            "course_code": "CSE101",
            "course_name": "Python Programming"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"CSE101" in response.data
    assert b"Python Programming" in response.data


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "healthy"
