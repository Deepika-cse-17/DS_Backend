# Student Report Card Management System

A comprehensive Student Report Card Management System implemented using various Abstract Data Types (ADTs) and Linear Data Structures. Available in both **Command-Line Interface** and **Web Application** versions.

## Data Structures Used

This project demonstrates the implementation and usage of the following data structures:

1. **Linked List** - Used to store and manage student records dynamically
2. **Stack** - Used for undo operations (LIFO - Last In First Out)
3. **Queue** - Used for processing operations in order (FIFO - First In First Out)
4. **List (Array)** - Used within each student's report card to store subjects and grades

## Features

- ✅ Add new students with unique IDs
- ✅ Remove students from the system
- ✅ Search students by ID or name
- ✅ Add subjects and grades to student report cards
- ✅ Update existing grades
- ✅ Display all students and their report cards
- ✅ Calculate average grades automatically
- ✅ Undo last delete operation (using Stack)
- ✅ Queue operations for batch processing
- ✅ View system statistics
- ✅ View undo stack and operation queue
- ✅ **Modern Web Interface** with responsive design
- ✅ **RESTful API** backend

## Project Structure

```
DS mini project/
│
├── student.py          # Student and ReportCard classes
├── linked_list.py      # Linked List implementation for students
├── stack.py            # Stack implementation for undo operations
├── queue.py            # Queue implementation for operation processing
├── main.py             # CLI version (command-line interface)
├── app.py              # Web application backend (Flask)
├── requirements.txt    # Python dependencies
│
├── templates/          # Frontend templates
│   └── index.html      # Main HTML page
│
├── static/             # Static files
│   ├── style.css       # CSS styling
│   └── script.js       # JavaScript frontend logic
│
└── README.md           # This file
```

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Steps

1. **Clone or download the project**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Docker Deployment

### Prerequisites for Docker

- Docker installed on your system
- Docker Compose (optional, for easier deployment)

### Quick Start with Docker

#### Option 1: Using Docker Compose (Recommended)

1. **Build and run the application:**
   ```bash
   docker-compose up --build
   ```

2. **Access the application:**
   ```
   http://localhost:5000
   ```

3. **Stop the application:**
   ```bash
   docker-compose down
   ```

#### Option 2: Using Docker directly

1. **Build the Docker image:**
   ```bash
   docker build -t student-report-card-system .
   ```

2. **Run the container:**
   ```bash
   docker run -d -p 5000:5000 --name student-report-card-system student-report-card-system
   ```

3. **Access the application:**
   ```
   http://localhost:5000
   ```

4. **View running containers:**
   ```bash
   docker ps
   ```

5. **Stop the container:**
   ```bash
   docker stop student-report-card-system
   ```

6. **Remove the container:**
   ```bash
   docker rm student-report-card-system
   ```

### Docker Commands Reference

- **View logs:**
  ```bash
  docker logs student-report-card-system
  ```

- **View logs in real-time:**
  ```bash
  docker logs -f student-report-card-system
  ```

- **Execute commands in container:**
  ```bash
  docker exec -it student-report-card-system bash
  ```

- **Rebuild after code changes:**
  ```bash
  docker-compose up --build
  ```

## Running the Application

### Web Application (Recommended)

1. **Start the Flask server:**
   ```bash
   python app.py
   ```

2. **Open your web browser and navigate to:**
   ```
   http://localhost:5000
   ```

3. **Use the web interface:**
   - Navigate between tabs: Students, Add Student, Search, Statistics, Data Structures
   - Add students and grades through the forms
   - View all students in a beautiful card layout
   - Search for students by ID or name
   - View system statistics
   - Monitor Stack and Queue operations

### Command-Line Interface

1. **Run the CLI version:**
   ```bash
   python main.py
   ```

2. **Follow the menu prompts** to interact with the system

## Web Application Features

### Frontend (HTML/CSS/JavaScript)

- **Modern, Responsive UI** - Works on desktop and mobile devices
- **Tab-based Navigation** - Easy access to all features
- **Real-time Updates** - Automatic refresh of data
- **Toast Notifications** - User-friendly feedback messages
- **Beautiful Card Layout** - Visual display of student information
- **Interactive Forms** - Easy data entry with validation

### Backend (Flask REST API)

- **RESTful API Endpoints:**
  - `GET /api/students` - Get all students
  - `POST /api/students` - Add a new student
  - `GET /api/students/<id>` - Get a specific student
  - `DELETE /api/students/<id>` - Delete a student
  - `GET /api/students/search?name=<name>` - Search by name
  - `POST /api/students/<id>/grades` - Add a grade
  - `PUT /api/students/<id>/grades` - Update a grade
  - `POST /api/undo` - Undo last delete
  - `GET /api/statistics` - Get system statistics
  - `GET /api/stack` - View undo stack
  - `GET /api/queue` - View operation queue
  - `POST /api/queue/process` - Process all queued operations

## Usage Guide

### Web Application

1. **Add Student:**
   - Go to "Add Student" tab
   - Enter Student ID and Name
   - Click "Add Student"

2. **Add Grades:**
   - Go to "Add Student" tab
   - Scroll to "Add Grade to Student"
   - Enter Student ID, Subject, and Grade (0-100)
   - Click "Add Grade"

3. **View Students:**
   - Go to "Students" tab
   - See all students in card format
   - Each card shows subjects, grades, and average

4. **Search:**
   - Go to "Search" tab
   - Search by ID or Name
   - Results displayed instantly

5. **Statistics:**
   - Go to "Statistics" tab
   - View system-wide statistics
   - See grade averages and counts

6. **Data Structures:**
   - Go to "Data Structures" tab
   - View Stack (LIFO) and Queue (FIFO)
   - Undo last delete or process queue

### Command-Line Interface

1. **Add Student** - Choose option 1, enter ID and name
2. **Remove Student** - Choose option 2, enter student ID
3. **Search Student by ID** - Choose option 3, enter student ID
4. **Search Student by Name** - Choose option 4, enter name
5. **Add Subject & Grade** - Choose option 5, enter details
6. **Update Grade** - Choose option 6, enter new grade
7. **Display All Students** - Choose option 7
8. **Display Student Report Card** - Choose option 8, enter ID
9. **Undo Last Delete** - Choose option 9
10. **Display Statistics** - Choose option 10
11. **View Undo Stack** - Choose option 11
12. **View Operation Queue** - Choose option 12
13. **Process Operation Queue** - Choose option 13
14. **Exit** - Choose option 14

## Example Workflow

1. **Add a student:** 
   - Web: Go to "Add Student" tab → Enter ID (e.g., "S001") and name (e.g., "John Doe") → Click "Add Student"
   - CLI: Choose option 1 → Enter ID and name

2. **Add grades:**
   - Web: Go to "Add Student" tab → Scroll to "Add Grade" → Enter student ID, subject (e.g., "Mathematics"), and grade (e.g., 85) → Click "Add Grade"
   - CLI: Choose option 5 → Enter details

3. **View report card:**
   - Web: Go to "Students" tab → See all students with their report cards
   - CLI: Choose option 8 → Enter student ID

4. **Remove student:**
   - Web: Click "Delete" button on student card
   - CLI: Choose option 2 → Enter student ID

5. **Undo delete:**
   - Web: Go to "Data Structures" tab → Click "Undo Last Delete"
   - CLI: Choose option 9

## Data Structure Implementations

### Linked List (linked_list.py)
- **Purpose**: Store student records dynamically
- **Operations**: Add, Remove, Search, Display
- **Time Complexity**: 
  - Add: O(n)
  - Search: O(n)
  - Remove: O(n)

### Stack (stack.py)
- **Purpose**: Undo operations (LIFO)
- **Operations**: Push, Pop, Peek
- **Time Complexity**: 
  - Push: O(1)
  - Pop: O(1)
  - Peek: O(1)

### Queue (queue.py)
- **Purpose**: Process operations in order (FIFO)
- **Operations**: Enqueue, Dequeue, Peek
- **Time Complexity**: 
  - Enqueue: O(1)
  - Dequeue: O(1)
  - Peek: O(1)

### List (student.py - ReportCard class)
- **Purpose**: Store subjects and grades for each student
- **Operations**: Add, Update, Get, Calculate Average
- **Time Complexity**: 
  - Add: O(1) amortized
  - Update: O(n) for search
  - Get: O(n) for search

## Requirements

### For Web Application
- Python 3.6 or higher
- Flask 3.0.0
- flask-cors 4.0.0

### For CLI Application
- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Notes

- Student IDs must be unique
- Grades must be between 0 and 100
- Subject names are case-sensitive
- The undo stack can hold up to 100 operations (configurable)
- The operation queue can hold up to 100 operations (configurable)
- Web application runs on `http://localhost:5000` by default
- All data is stored in memory (not persisted to disk)

## Technology Stack

### Backend
- **Python 3** - Programming language
- **Flask** - Web framework
- **Flask-CORS** - Cross-Origin Resource Sharing support

### Frontend
- **HTML5** - Markup
- **CSS3** - Styling with modern features (Grid, Flexbox, Animations)
- **JavaScript (ES6+)** - Frontend logic and API communication
- **Fetch API** - For REST API calls

## Author

Created as a Data Structures mini project demonstrating ADTs and Linear Data Structures with both CLI and Web interfaces.
