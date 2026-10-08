import pytest
from database.db import db
from app.services.academic_service import AcademicService

@pytest.fixture(autouse=True)
def reset_db():
    db.reset()
    yield
    db.reset()

def test_enrollment_success():
    enrollment = AcademicService.enroll_student("S101", "C101", 3)
    assert enrollment["status"] == "ACTIVE"

def test_credit_limit_enforced():
    AcademicService.add_course("C103", "AI", 10, "F101")
    AcademicService.add_course("C104", "Cloud", 8, "F101")
    AcademicService.enroll_student("S101", "C103", 3)
    AcademicService.enroll_student("S101", "C104", 3)

    with pytest.raises(ValueError, match="Credit limit exceeded"):
        AcademicService.enroll_student("S101", "C101", 3)

def test_duplicate_enrollment_fails():
    AcademicService.enroll_student("S101", "C101", 3)
    with pytest.raises(ValueError, match="already enrolled"):
        AcademicService.enroll_student("S101", "C101", 3)
