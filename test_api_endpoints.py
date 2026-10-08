from app import create_app
from database.db import db

def test_health_endpoint():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        db.reset()
        response = client.get("/api/health")
        assert response.status_code == 200
        assert response.get_json()["status"] == "UP"

def test_list_courses():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        db.reset()
        response = client.get("/api/courses")
        assert response.status_code == 200
        assert response.get_json()["count"] >= 2

def test_enroll_endpoint():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        db.reset()
        response = client.post("/api/enroll",
                               json={"student_id": "S101", "course_id": "C101", "semester": 3})
        assert response.status_code == 201
