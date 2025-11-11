"""
Stack Implementation for Undo Operations
Used to store deleted or modified students for undo functionality
"""

from student import Student

class StackNode:
    """Node class for Stack"""
    
    def __init__(self, data, operation_type="delete"):
        self.data = data  # Student object
        self.operation_type = operation_type  # "delete" or "modify"
        self.next = None


class UndoStack:
    """Stack ADT for managing undo operations"""
    
    def __init__(self, max_size=100):
        self.top = None
        self.size = 0
        self.max_size = max_size
    
    def is_empty(self):
        """Check if the stack is empty"""
        return self.top is None
    
    def is_full(self):
        """Check if the stack is full"""
        return self.size >= self.max_size
    
    def push(self, student, operation_type="delete"):
        """Push a student onto the stack"""
        if self.is_full():
            # Remove oldest item (bottom of stack)
            self._remove_bottom()
        
        new_node = StackNode(student, operation_type)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        return True
    
    def pop(self):
        """Pop a student from the stack"""
        if self.is_empty():
            return None
        
        popped_node = self.top
        self.top = self.top.next
        self.size -= 1
        return popped_node
    
    def peek(self):
        """Peek at the top of the stack without removing"""
        if self.is_empty():
            return None
        return self.top
    
    def _remove_bottom(self):
        """Remove the bottom element when stack is full"""
        if self.size <= 1:
            self.top = None
            self.size = 0
            return
        
        current = self.top
        while current.next.next is not None:
            current = current.next
        current.next = None
        self.size -= 1
    
    def get_size(self):
        """Get the size of the stack"""
        return self.size
    
    def clear(self):
        """Clear the stack"""
        self.top = None
        self.size = 0
    
    def display(self):
        """Display all items in the stack (for debugging)"""
        if self.is_empty():
            return "Stack is empty."
        
        result = f"\nUndo Stack (Size: {self.size}):\n"
        result += "-" * 40 + "\n"
        current = self.top
        index = 1
        while current is not None:
            result += f"[{index}] {current.operation_type.upper()}: {current.data.name} (ID: {current.data.student_id})\n"
            current = current.next
            index += 1
        return result

