"""
Student Report Card Management System
Main program that integrates all data structures:
- Linked List: For storing student records
- Stack: For undo operations
- Queue: For processing operations
- List: For storing subjects and grades within each student
"""

import copy
from student import Student
from linked_list import StudentLinkedList
from stack import UndoStack
from queue import OperationQueue


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
        # Check if student already exists
        if self.student_list.search_student(student_id) is not None:
            return False, f"Student with ID {student_id} already exists!"
        
        student = Student(student_id, name)
        self.student_list.add_student(student)
        
        # Add to operation queue
        self.operation_queue.enqueue(student, "add")
        
        return True, f"Student {name} (ID: {student_id}) added successfully!"
    
    def remove_student(self, student_id):
        """Remove a student from the system"""
        student = self.student_list.remove_student(student_id)
        
        if student is None:
            return False, f"Student with ID {student_id} not found!"
        
        # Push to undo stack for potential undo
        self.undo_stack.push(student, "delete")
        
        # Add to operation queue
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
            # Add to operation queue
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
        
        # Store old student state for undo
        old_student = copy.deepcopy(student)
        
        if student.update_subject_grade(subject, new_grade):
            # Push old state to undo stack
            self.undo_stack.push(old_student, "modify")
            
            # Add to operation queue
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
        
        # Restore student
        self.student_list.add_student(student)
        
        return True, f"Undone: Student {student.name} (ID: {student.student_id}) restored!"
    
    def display_all_students(self):
        """Display all students"""
        return self.student_list.display_all()
    
    def display_statistics(self):
        """Display system statistics"""
        stats = f"\n{'='*60}\n"
        stats += "SYSTEM STATISTICS\n"
        stats += f"{'='*60}\n"
        stats += f"Total Students: {self.student_list.get_size()}\n"
        stats += f"Undo Stack Size: {self.undo_stack.get_size()}\n"
        stats += f"Operation Queue Size: {self.operation_queue.get_size()}\n"
        
        if self.student_list.get_size() > 0:
            students = self.student_list.get_all_students()
            averages = [s.get_average() for s in students]
            if averages:
                stats += f"\nAverage Grade Statistics:\n"
                stats += f"  Highest Average: {max(averages):.2f}\n"
                stats += f"  Lowest Average: {min(averages):.2f}\n"
                stats += f"  Overall Average: {sum(averages)/len(averages):.2f}\n"
        
        stats += f"{'='*60}\n"
        return stats
    
    def process_queue(self):
        """Process all operations in the queue"""
        if self.operation_queue.is_empty():
            return "No operations in queue to process."
        
        operations = self.operation_queue.process_all()
        result = f"\nProcessed {len(operations)} operations from queue:\n"
        result += "-" * 40 + "\n"
        for i, op in enumerate(operations, 1):
            if op and op.data:
                if isinstance(op.data, Student):
                    result += f"[{i}] {op.operation_type.upper()}: {op.data.name} (ID: {op.data.student_id})\n"
                else:
                    result += f"[{i}] {op.operation_type.upper()}: {op.data}\n"
        return result


def print_menu():
    """Print the main menu"""
    print("\n" + "="*60)
    print("    STUDENT REPORT CARD MANAGEMENT SYSTEM")
    print("="*60)
    print("1.  Add Student")
    print("2.  Remove Student")
    print("3.  Search Student by ID")
    print("4.  Search Student by Name")
    print("5.  Add Subject & Grade")
    print("6.  Update Grade")
    print("7.  Display All Students")
    print("8.  Display Student Report Card")
    print("9.  Undo Last Delete")
    print("10. Display Statistics")
    print("11. View Undo Stack")
    print("12. View Operation Queue")
    print("13. Process Operation Queue")
    print("14. Exit")
    print("="*60)


def main():
    """Main function to run the program"""
    system = ReportCardManagementSystem()
    
    print("\nWelcome to Student Report Card Management System!")
    print("This system uses:")
    print("  - Linked List: For storing student records")
    print("  - Stack: For undo operations")
    print("  - Queue: For processing operations")
    print("  - List: For storing subjects and grades")
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-14): ").strip()
        
        if choice == '1':
            # Add Student
            try:
                student_id = input("Enter Student ID: ").strip()
                name = input("Enter Student Name: ").strip()
                if student_id and name:
                    success, message = system.add_student(student_id, name)
                    print(f"\n{message}")
                else:
                    print("\nError: Student ID and Name cannot be empty!")
            except Exception as e:
                print(f"\nError: {e}")
        
        elif choice == '2':
            # Remove Student
            try:
                student_id = input("Enter Student ID to remove: ").strip()
                if student_id:
                    success, message = system.remove_student(student_id)
                    print(f"\n{message}")
                else:
                    print("\nError: Student ID cannot be empty!")
            except Exception as e:
                print(f"\nError: {e}")
        
        elif choice == '3':
            # Search Student by ID
            try:
                student_id = input("Enter Student ID to search: ").strip()
                if student_id:
                    student, error = system.search_student(student_id)
                    if error:
                        print(f"\n{error}")
                    else:
                        print(student.display())
                else:
                    print("\nError: Student ID cannot be empty!")
            except Exception as e:
                print(f"\nError: {e}")
        
        elif choice == '4':
            # Search Student by Name
            try:
                name = input("Enter Student Name to search: ").strip()
                if name:
                    results, error = system.search_by_name(name)
                    if error:
                        print(f"\n{error}")
                    else:
                        print(f"\nFound {len(results)} student(s):")
                        for student in results:
                            print(student.display())
                else:
                    print("\nError: Name cannot be empty!")
            except Exception as e:
                print(f"\nError: {e}")
        
        elif choice == '5':
            # Add Subject & Grade
            try:
                student_id = input("Enter Student ID: ").strip()
                subject = input("Enter Subject Name: ").strip()
                grade = float(input("Enter Grade (0-100): ").strip())
                if student_id and subject:
                    success, message = system.add_grade(student_id, subject, grade)
                    print(f"\n{message}")
                else:
                    print("\nError: Student ID and Subject cannot be empty!")
            except ValueError:
                print("\nError: Grade must be a number!")
            except Exception as e:
                print(f"\nError: {e}")
        
        elif choice == '6':
            # Update Grade
            try:
                student_id = input("Enter Student ID: ").strip()
                subject = input("Enter Subject Name: ").strip()
                new_grade = float(input("Enter New Grade (0-100): ").strip())
                if student_id and subject:
                    success, message = system.update_grade(student_id, subject, new_grade)
                    print(f"\n{message}")
                else:
                    print("\nError: Student ID and Subject cannot be empty!")
            except ValueError:
                print("\nError: Grade must be a number!")
            except Exception as e:
                print(f"\nError: {e}")
        
        elif choice == '7':
            # Display All Students
            print(system.display_all_students())
        
        elif choice == '8':
            # Display Student Report Card
            try:
                student_id = input("Enter Student ID: ").strip()
                if student_id:
                    student, error = system.search_student(student_id)
                    if error:
                        print(f"\n{error}")
                    else:
                        print(student.display())
                else:
                    print("\nError: Student ID cannot be empty!")
            except Exception as e:
                print(f"\nError: {e}")
        
        elif choice == '9':
            # Undo Last Delete
            success, message = system.undo_last_delete()
            print(f"\n{message}")
        
        elif choice == '10':
            # Display Statistics
            print(system.display_statistics())
        
        elif choice == '11':
            # View Undo Stack
            print(system.undo_stack.display())
        
        elif choice == '12':
            # View Operation Queue
            print(system.operation_queue.display())
        
        elif choice == '13':
            # Process Operation Queue
            print(system.process_queue())
        
        elif choice == '14':
            # Exit
            print("\nThank you for using Student Report Card Management System!")
            print("Goodbye!")
            break
        
        else:
            print("\nInvalid choice! Please enter a number between 1-14.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()

