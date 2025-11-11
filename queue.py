"""
Queue Implementation for Operation Processing
Used to process student operations in FIFO order
"""

from student import Student

class QueueNode:
    """Node class for Queue"""
    
    def __init__(self, data, operation_type="add"):
        self.data = data  # Student object or operation data
        self.operation_type = operation_type  # "add", "update", "delete", etc.
        self.next = None


class OperationQueue:
    """Queue ADT for managing operations in FIFO order"""
    
    def __init__(self, max_size=100):
        self.front = None
        self.rear = None
        self.size = 0
        self.max_size = max_size
    
    def is_empty(self):
        """Check if the queue is empty"""
        return self.front is None
    
    def is_full(self):
        """Check if the queue is full"""
        return self.size >= self.max_size
    
    def enqueue(self, student, operation_type="add"):
        """Add an operation to the queue"""
        if self.is_full():
            return False
        
        new_node = QueueNode(student, operation_type)
        
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self.size += 1
        return True
    
    def dequeue(self):
        """Remove and return the front operation from the queue"""
        if self.is_empty():
            return None
        
        dequeued_node = self.front
        
        if self.front == self.rear:
            # Only one element
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        
        self.size -= 1
        return dequeued_node
    
    def peek(self):
        """Peek at the front of the queue without removing"""
        if self.is_empty():
            return None
        return self.front
    
    def get_size(self):
        """Get the size of the queue"""
        return self.size
    
    def clear(self):
        """Clear the queue"""
        self.front = None
        self.rear = None
        self.size = 0
    
    def display(self):
        """Display all operations in the queue"""
        if self.is_empty():
            return "Queue is empty."
        
        result = f"\nOperation Queue (Size: {self.size}):\n"
        result += "-" * 40 + "\n"
        current = self.front
        index = 1
        while current is not None:
            if isinstance(current.data, Student):
                result += f"[{index}] {current.operation_type.upper()}: {current.data.name} (ID: {current.data.student_id})\n"
            else:
                result += f"[{index}] {current.operation_type.upper()}: {current.data}\n"
            current = current.next
            index += 1
        return result
    
    def process_all(self):
        """Process all operations in the queue and return them"""
        operations = []
        while not self.is_empty():
            operations.append(self.dequeue())
        return operations

