# Gradebook Management System

A Python console application built for teachers to manage student records, input assignment grades, calculate statistics, and export reports securely.

## 1. User Guide & Installation
1. Open the project terminal interface.
2. Run `python database.py` to initialize the database architecture.
3. Run `python main.py` to start the interactive console application.
4. Follow the numerical menu prompts (1-6) to manage classroom data.

## 2. Database Schema
The persistence layer utilizes SQLite with two relational data tables:
- **`students` table:** Holds identification data.
  - `student_id` (INTEGER, Primary Key, Autoincrement)
  - `name` (TEXT)
- **`grades` table:** Holds structural assignment data.
  - `grade_id` (INTEGER, Primary Key, Autoincrement)
  - `student_id` (INTEGER, Foreign Key referencing `students`)
  - `assignment_name` (TEXT)
  - `score` (REAL)

## 3. Class Diagram & OOP Design
The architecture utilizes standard object-oriented programming layout:
```text
   +---------------------------------------+
   |                Person                 |
   +---------------------------------------+
   | - _name: str                          |
   +---------------------------------------+
   | + get_name() / set_name()             |
   | + __str__()                           |
   +---------------------------------------+
                       ^
                       | (Inheritance)
                       |
   +---------------------------------------+
   |                Student                |
   +---------------------------------------+
   | - __student_id: int                   |
   | + grades: dict                        |
   +---------------------------------------+
   | + get_student_id()                    |
   | + add_grade(assignment, score)        |
   | + calculate_average()                 |
   | + __str__()                           |
   +---------------------------------------+
  
## 4. Test Report
Verification testing matrix has been completely compiled and verified.