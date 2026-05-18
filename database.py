import sqlite3

# Connects to the local database file
def connect_db():
    return sqlite3.connect("gradebook.db")

# Sets up the database tables if they aren't created yet
def initialize_database():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Base table to store student names
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    
    # Linked table for grades using student_id as a foreign key
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            assignment_name TEXT NOT NULL,
            score REAL NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students (student_id) ON DELETE CASCADE
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

if __name__ == "__main__":
    initialize_database()