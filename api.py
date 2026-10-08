from flask import Blueprint, request, jsonify
from app.services.academic_service import AcademicService

api_bp = Blueprint("api", __name__)

@api_bp.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "UP",
        "service": "Enterprise Student Record & Academic Management Platform",
        "version": "1.0.0"
    }), 200

@api_bp.route("/students", methods=["POST"])
def add_student():
    data = request.get_json() or {}
    try:
        student = AcademicService.add_student(
            data.get("student_id"), data.get("name"),
            data.get("email"), int(data.get("semester", 1))
        )
        return jsonify({"message": "Student added successfully", "student": student}), 201
    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e)}), 400

@api_bp.route("/students/<student_id>", methods=["GET"])
def get_student(student_id):
    student = AcademicService.get_student(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student), 200

@api_bp.route("/courses", methods=["GET"])
def list_courses():
    return jsonify({"count": len(AcademicService.list_courses()),
                    "courses": AcademicService.list_courses()}), 200

@api_bp.route("/courses", methods=["POST"])
def add_course():
    data = request.get_json() or {}
    try:
        course = AcademicService.add_course(
            data.get("course_id"), data.get("name"),
            int(data.get("credits", 0)), data.get("faculty_id")
        )
        return jsonify({"message": "Course added successfully", "course": course}), 201
    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e)}), 400

@api_bp.route("/enroll", methods=["POST"])
def enroll():
    data = request.get_json() or {}
    try:
        enrollment = AcademicService.enroll_student(
            data.get("student_id"), data.get("course_id"), data.get("semester")
        )
        return jsonify({"message": "Enrollment successful", "enrollment": enrollment}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@api_bp.route("/grades", methods=["POST"])
def add_grade():
    data = request.get_json() or {}
    try:
        grade = AcademicService.add_grade(
            data.get("student_id"), data.get("course_id"), data.get("grade")
        )
        return jsonify({"message": "Grade recorded successfully", "grade": grade}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
