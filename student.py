"""
Student and ReportCard Classes
Represents a student with their report card information
"""

class ReportCard:
    """Represents a report card with subjects and grades"""
    
    def __init__(self):
        # Using List (array) to store subjects and grades
        self.subjects = []  # List of subject names
        self.grades = []    # List of corresponding grades
        
    def add_subject(self, subject, grade):
        """Add a subject and grade to the report card"""
        if subject not in self.subjects:
            self.subjects.append(subject)
            self.grades.append(grade)
            return True
        return False
    
    def update_grade(self, subject, new_grade):
        """Update grade for a specific subject"""
        if subject in self.subjects:
            index = self.subjects.index(subject)
            self.grades[index] = new_grade
            return True
        return False
    
    def get_grade(self, subject):
        """Get grade for a specific subject"""
        if subject in self.subjects:
            index = self.subjects.index(subject)
            return self.grades[index]
        return None
    
    def calculate_average(self):
        """Calculate average of all grades"""
        if len(self.grades) == 0:
            return 0.0
        return sum(self.grades) / len(self.grades)
    
    def get_all_subjects(self):
        """Get all subjects"""
        return self.subjects.copy()
    
    def display(self):
        """Display the report card"""
        if len(self.subjects) == 0:
            return "No subjects added yet."
        
        result = "\nReport Card:\n"
        result += "-" * 40 + "\n"
        for i in range(len(self.subjects)):
            result += f"{self.subjects[i]}: {self.grades[i]}\n"
        result += "-" * 40 + "\n"
        result += f"Average: {self.calculate_average():.2f}\n"
        return result
    
    def __str__(self):
        return self.display()


class Student:
    """Represents a student with ID, name, and report card"""
    
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.report_card = ReportCard()
    
    def add_subject_grade(self, subject, grade):
        """Add a subject and grade to student's report card"""
        return self.report_card.add_subject(subject, grade)
    
    def update_subject_grade(self, subject, new_grade):
        """Update grade for a subject"""
        return self.report_card.update_grade(subject, new_grade)
    
    def get_average(self):
        """Get student's average grade"""
        return self.report_card.calculate_average()
    
    def display(self):
        """Display student information and report card"""
        result = f"\n{'='*50}\n"
        result += f"Student ID: {self.student_id}\n"
        result += f"Student Name: {self.name}\n"
        result += self.report_card.display()
        result += f"{'='*50}\n"
        return result
    
    def __str__(self):
        return self.display()
    
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False

