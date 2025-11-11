"""
Flask Backend for Student Report Card Management System
RESTful API that uses all data structures: Linked List, Stack, Queue, List
"""

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import copy
from student import Student
from linked_list import StudentLinkedList
from stack import UndoStack
from queue import OperationQueue

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication


class ReportCardManagementSystem:
    """Main management system integrating all data structures"""
    
    def __init__(self):
        # Linked List for storing all students
        self.student_list = StudentLinkedList()
        
        # Stack for undo operations
        self.undo_stack = UndoStack()
        
        # Queue for processing operations
        self.operation_queue = OperationQueue()
    
    def add_student(self, student_id, name):
        """Add a new student to the system"""
        if self.student_list.search_student(student_id) is not None:
            return False, f"Student with ID {student_id} already exists!"
        
        student = Student(student_id, name)
        self.student_list.add_student(student)
        self.operation_queue.enqueue(student, "add")
        return True, f"Student {name} (ID: {student_id}) added successfully!"
    
    def remove_student(self, student_id):
        """Remove a student from the system"""
        student = self.student_list.remove_student(student_id)
        
        if student is None:
            return False, f"Student with ID {student_id} not found!"
        
        self.undo_stack.push(student, "delete")
        self.operation_queue.enqueue(student, "delete")
        return True, f"Student {student.name} (ID: {student_id}) removed successfully!"
    
    def search_student(self, student_id):
        """Search for a student by ID"""
        student = self.student_list.search_student(student_id)
        if student is None:
            return None, f"Student with ID {student_id} not found!"
        return student, None
    
    def search_by_name(self, name):
        """Search for students by name"""
        results = self.student_list.search_by_name(name)
        if len(results) == 0:
            return [], f"No students found with name containing '{name}'"
        return results, None
    
    def add_grade(self, student_id, subject, grade):
        """Add a subject and grade to a student's report card"""
        student = self.student_list.search_student(student_id)
        if student is None:
            return False, f"Student with ID {student_id} not found!"
        
        if not (0 <= grade <= 100):
            return False, "Grade must be between 0 and 100!"
        
        if student.add_subject_grade(subject, grade):
            self.operation_queue.enqueue(student, "add_grade")
            return True, f"Grade {grade} added for {subject}!"
        else:
            return False, f"Subject {subject} already exists! Use update instead."
    
    def update_grade(self, student_id, subject, new_grade):
        """Update a grade for a student"""
        student = self.student_list.search_student(student_id)
        if student is None:
            return False, f"Student with ID {student_id} not found!"
        
        if not (0 <= new_grade <= 100):
            return False, "Grade must be between 0 and 100!"
        
        old_grade = student.report_card.get_grade(subject)
        if old_grade is None:
            return False, f"Subject {subject} not found for this student!"
        
        old_student = copy.deepcopy(student)
        
        if student.update_subject_grade(subject, new_grade):
            self.undo_stack.push(old_student, "modify")
            self.operation_queue.enqueue(student, "update_grade")
            return True, f"Grade for {subject} updated from {old_grade} to {new_grade}!"
        else:
            return False, "Failed to update grade!"
    
    def undo_last_delete(self):
        """Undo the last delete operation"""
        if self.undo_stack.is_empty():
            return False, "No operations to undo!"
        
        top_node = self.undo_stack.peek()
        if top_node.operation_type != "delete":
            return False, "Last operation was not a delete. Cannot undo!"
        
        popped_node = self.undo_stack.pop()
        student = popped_node.data
        self.student_list.add_student(student)
        return True, f"Undone: Student {student.name} (ID: {student.student_id}) restored!"
    
    def get_all_students(self):
        """Get all students as a list"""
        return self.student_list.get_all_students()
    
    def get_statistics(self):
        """Get system statistics"""
        stats = {
            "total_students": self.student_list.get_size(),
            "undo_stack_size": self.undo_stack.get_size(),
            "queue_size": self.operation_queue.get_size(),
            "highest_average": 0,
            "lowest_average": 0,
            "overall_average": 0
        }
        
        if self.student_list.get_size() > 0:
            students = self.student_list.get_all_students()
            averages = [s.get_average() for s in students if s.report_card.get_all_subjects()]
            if averages:
                stats["highest_average"] = round(max(averages), 2)
                stats["lowest_average"] = round(min(averages), 2)
                stats["overall_average"] = round(sum(averages) / len(averages), 2)
        
        return stats


# Initialize the management system
system = ReportCardManagementSystem()


# API Routes

@app.route('/api/students', methods=['GET'])
def get_all_students():
    """Get all students"""
    students = system.get_all_students()
    students_data = []
    for student in students:
        students_data.append({
            "student_id": student.student_id,
            "name": student.name,
            "subjects": student.report_card.subjects,
            "grades": student.report_card.grades,
            "average": round(student.get_average(), 2)
        })
    return jsonify({"success": True, "students": students_data})


@app.route('/api/students', methods=['POST'])
def add_student():
    """Add a new student"""
    data = request.json
    student_id = data.get('student_id', '').strip()
    name = data.get('name', '').strip()
    
    if not student_id or not name:
        return jsonify({"success": False, "message": "Student ID and Name are required!"}), 400
    
    success, message = system.add_student(student_id, name)
    if success:
        return jsonify({"success": True, "message": message}), 201
    else:
        return jsonify({"success": False, "message": message}), 400


@app.route('/api/students/<student_id>', methods=['GET'])
def get_student(student_id):
    """Get a specific student by ID"""
    student, error = system.search_student(student_id)
    if error:
        return jsonify({"success": False, "message": error}), 404
    
    return jsonify({
        "success": True,
        "student": {
            "student_id": student.student_id,
            "name": student.name,
            "subjects": student.report_card.subjects,
            "grades": student.report_card.grades,
            "average": round(student.get_average(), 2)
        }
    })


@app.route('/api/students/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    """Delete a student"""
    success, message = system.remove_student(student_id)
    if success:
        return jsonify({"success": True, "message": message}), 200
    else:
        return jsonify({"success": False, "message": message}), 404


@app.route('/api/students/search', methods=['GET'])
def search_students():
    """Search students by name"""
    name = request.args.get('name', '').strip()
    if not name:
        return jsonify({"success": False, "message": "Name parameter is required!"}), 400
    
    results, error = system.search_by_name(name)
    if error:
        return jsonify({"success": False, "message": error}), 404
    
    students_data = []
    for student in results:
        students_data.append({
            "student_id": student.student_id,
            "name": student.name,
            "subjects": student.report_card.subjects,
            "grades": student.report_card.grades,
            "average": round(student.get_average(), 2)
        })
    
    return jsonify({"success": True, "students": students_data})


@app.route('/api/students/<student_id>/grades', methods=['POST'])
def add_grade(student_id):
    """Add a grade to a student's report card"""
    data = request.json
    subject = data.get('subject', '').strip()
    grade = data.get('grade')
    
    if not subject:
        return jsonify({"success": False, "message": "Subject is required!"}), 400
    
    try:
        grade = float(grade)
    except (ValueError, TypeError):
        return jsonify({"success": False, "message": "Grade must be a number!"}), 400
    
    success, message = system.add_grade(student_id, subject, grade)
    if success:
        return jsonify({"success": True, "message": message}), 201
    else:
        return jsonify({"success": False, "message": message}), 400


@app.route('/api/students/<student_id>/grades', methods=['PUT'])
def update_grade(student_id):
    """Update a grade for a student"""
    data = request.json
    subject = data.get('subject', '').strip()
    grade = data.get('grade')
    
    if not subject:
        return jsonify({"success": False, "message": "Subject is required!"}), 400
    
    try:
        grade = float(grade)
    except (ValueError, TypeError):
        return jsonify({"success": False, "message": "Grade must be a number!"}), 400
    
    success, message = system.update_grade(student_id, subject, grade)
    if success:
        return jsonify({"success": True, "message": message}), 200
    else:
        return jsonify({"success": False, "message": message}), 400


@app.route('/api/undo', methods=['POST'])
def undo_delete():
    """Undo last delete operation"""
    success, message = system.undo_last_delete()
    if success:
        return jsonify({"success": True, "message": message}), 200
    else:
        return jsonify({"success": False, "message": message}), 400


@app.route('/api/statistics', methods=['GET'])
def get_statistics():
    """Get system statistics"""
    stats = system.get_statistics()
    return jsonify({"success": True, "statistics": stats})


@app.route('/api/queue', methods=['GET'])
def get_queue():
    """Get operation queue"""
    operations = []
    current = system.operation_queue.front
    while current is not None:
        if isinstance(current.data, Student):
            operations.append({
                "operation_type": current.operation_type,
                "student_id": current.data.student_id,
                "student_name": current.data.name
            })
        current = current.next
    
    return jsonify({"success": True, "queue": operations, "size": system.operation_queue.get_size()})


@app.route('/api/stack', methods=['GET'])
def get_stack():
    """Get undo stack"""
    operations = []
    current = system.undo_stack.top
    while current is not None:
        if isinstance(current.data, Student):
            operations.append({
                "operation_type": current.operation_type,
                "student_id": current.data.student_id,
                "student_name": current.data.name
            })
        current = current.next
    
    return jsonify({"success": True, "stack": operations, "size": system.undo_stack.get_size()})


@app.route('/api/queue/process', methods=['POST'])
def process_queue():
    """Process all operations in queue"""
    operations = system.operation_queue.process_all()
    processed = []
    for op in operations:
        if op and op.data:
            if isinstance(op.data, Student):
                processed.append({
                    "operation_type": op.operation_type,
                    "student_id": op.data.student_id,
                    "student_name": op.data.name
                })
    
    return jsonify({"success": True, "message": f"Processed {len(processed)} operations", "operations": processed})


@app.route('/')
def index():
    """Serve the main HTML page"""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
