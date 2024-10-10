import sqlite3

# Verbindung zur Datenbank herstellen/Cursor festlegen um DB zu managen
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Cursor
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        course TEXT NOT NULL
    )
''')

# Erste Funktion hizufügen (CREATE)
def add_student (name, age, course):
    cursor.execute('''
    INSERT INTO Students (name, age, course) VALUES (?, ?, ?)        
    ''', (name, age, course))
    conn.commit()
    print(f"{name} wurde Hinzugefügt")