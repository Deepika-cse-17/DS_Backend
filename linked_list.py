"""
Linked List Implementation for Student Records
Each node contains a Student object
"""

from student import Student

class Node:
    """Node class for Linked List"""
    
    def __init__(self, data):
        self.data = data  # Student object
        self.next = None


class StudentLinkedList:
    """Linked List ADT for managing student records"""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        """Check if the linked list is empty"""
        return self.head is None
    
    def add_student(self, student):
        """Add a student to the linked list (at the end)"""
        new_node = Node(student)
        
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        
        self.size += 1
        return True
    
    def remove_student(self, student_id):
        """Remove a student by ID from the linked list"""
        if self.is_empty():
            return None
        
        # If head node is to be removed
        if self.head.data.student_id == student_id:
            removed_student = self.head.data
            self.head = self.head.next
            self.size -= 1
            return removed_student
        
        # Search for the node to remove
        current = self.head
        while current.next is not None:
            if current.next.data.student_id == student_id:
                removed_student = current.next.data
                current.next = current.next.next
                self.size -= 1
                return removed_student
            current = current.next
        
        return None
    
    def search_student(self, student_id):
        """Search for a student by ID"""
        current = self.head
        while current is not None:
            if current.data.student_id == student_id:
                return current.data
            current = current.next
        return None
    
    def search_by_name(self, name):
        """Search for students by name (can return multiple)"""
        results = []
        current = self.head
        while current is not None:
            if name.lower() in current.data.name.lower():
                results.append(current.data)
            current = current.next
        return results
    
    def display_all(self):
        """Display all students in the linked list"""
        if self.is_empty():
            return "No students found."
        
        result = f"\nTotal Students: {self.size}\n"
        result += "=" * 60 + "\n"
        current = self.head
        index = 1
        while current is not None:
            result += f"\n[{index}] {current.data.display()}\n"
            current = current.next
            index += 1
        return result
    
    def get_all_students(self):
        """Get a list of all students"""
        students = []
        current = self.head
        while current is not None:
            students.append(current.data)
            current = current.next
        return students
    
    def get_size(self):
        """Get the size of the linked list"""
        return self.size
    
    def clear(self):
        """Clear all students from the linked list"""
        self.head = None
        self.size = 0

