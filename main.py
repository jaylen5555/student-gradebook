import os
import csv
from database import connect_db
from models import Student

class InvalidGradeError(Exception):
    pass

def add_student(name):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name) VALUES (?)", (name,))
        conn.commit()
        conn.close()
        print(f"Student '{name}' added successfully.")
    except Exception as e:
        print(f"Error adding student: {e}")

def add_grade(student_id, assignment, score):
    try:
        if score < 0 or score > 100:
            raise InvalidGradeError("Grade must be between 0 and 100.")
        
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM students WHERE student_id = ?", (student_id,))
        if not cursor.fetchone():
            print("Student ID not found.")
            conn.close()
            return

        cursor.execute(
            "INSERT INTO grades (student_id, assignment_name, score) VALUES (?, ?, ?)",
            (student_id, assignment, score)
        )
        conn.commit()
        conn.close()
        print("Grade added successfully.")
    except InvalidGradeError as ie:
        print(f"Validation Error: {ie}")
    except Exception as e:
        print(f"Error adding grade: {e}")

def get_student_report(student_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM students WHERE student_id = ?", (student_id,))
        student_row = cursor.fetchone()
        
        if not student_row:
            print("Student ID not found.")
            conn.close()
            return None

        student = Student(student_id, student_row[0])
        cursor.execute("SELECT assignment_name, score FROM grades WHERE student_id = ?", (student_id,))
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            student.add_grade(row[0], row[1])
        return student
    except Exception as e:
        print(f"Error fetching report: {e}")
        return None

def delete_student(student_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
        conn.commit()
        conn.close()
        print("Student record deleted.")
    except Exception as e:
        print(f"Error deleting student: {e}")

def export_to_csv(filename="grade_report.csv"):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT students.student_id, students.name, grades.assignment_name, grades.score 
            FROM students 
            LEFT JOIN grades ON students.student_id = grades.student_id
        ''')
        rows = cursor.fetchall()
        conn.close()

        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Student ID", "Name", "Assignment", "Score"])
            writer.writerows(rows)
        print(f"Report exported successfully to {filename}")
    except Exception as e:
        print(f"Error exporting file: {e}")

def main_menu():
    while True:
        print("\n--- GRADEBOOK MANAGEMENT SYSTEM ---")
        print("1. Add Student")
        print("2. Add Assignment Grade")
        print("3. View Student Progress Report")
        print("4. Delete Student Record")
        print("5. Export Report to CSV")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ")
        
        if choice == "1":
            name = input("Enter student name: ")
            if name.strip():
                add_student(name)
        elif choice == "2":
            try:
                sid = int(input("Enter student ID: "))
                asm = input("Enter assignment name: ")
                scr = float(input("Enter score: "))
                add_grade(sid, asm, scr)
            except ValueError:
                print("Invalid input. IDs must be integers and scores must be numbers.")
        elif choice == "3":
            try:
                sid = int(input("Enter student ID: "))
                student = get_student_report(sid)
                if student:
                    print("\n" + str(student))
                    print("Grades:", student.get_grades())
            except ValueError:
                print("Invalid ID format.")
        elif choice == "4":
            try:
                sid = int(input("Enter student ID to delete: "))
                delete_student(sid)
            except ValueError:
                print("Invalid ID format.")
        elif choice == "5":
            export_to_csv()
        elif choice == "6":
            print("Exiting application.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main_menu()