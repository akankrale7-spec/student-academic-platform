import pytest
from database.db import db
from app.services.academic_service import AcademicService

@pytest.fixture(autouse=True)
def reset_db():
    db.reset()
    yield
    db.reset()

def test_add_student():
    student = AcademicService.add_student("S200", "Grace Hopper", "grace@edu.com", 3)
    assert student["student_id"] == "S200"

def test_duplicate_student_fails():
    with pytest.raises(ValueError, match="already exists"):
        AcademicService.add_student("S101", "Duplicate", "dup@edu.com", 3)
