import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Create a table named DS3860 to store questions and answers
cursor.execute('''
CREATE TABLE IF NOT EXISTS DS3860 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL
)
''')

# Function to insert a question into the DS3860 table
def insert_question(question, option_a, option_b, option_c, option_d, correct_answer):
    cursor.execute('''
    INSERT INTO DS3860 (question, option_a, option_b, option_c, option_d, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (question, option_a, option_b, option_c, option_d, correct_answer))
    conn.commit()

# Questions in DB
questions = [
    ("Which MySQL command is used to create a new database?", 
     "CREATE DATABASE", "NEW DATABASE", "ADD DATABASE", "MAKE DATABASE", "A"),
    
    ("What is the function of the SELECT statement in MySQL?", 
     "To insert data", "To update data", "To retrieve data", "To delete data", "C"),
    
    ("Which SQL clause is used to filter records?", 
     "WHERE", "FILTER", "HAVING", "ORDER BY", "A"),
    
    ("What command is used to delete a table in MySQL?", 
     "REMOVE TABLE", "DELETE TABLE", "DROP TABLE", "CLEAR TABLE", "C"),
    
    ("Which function is used to count the number of rows in a MySQL query?", 
     "SUM()", "COUNT()", "TOTAL()", "NUMBER()", "B"),
    
    ("What does the acronym SQL stand for?", 
     "Structured Query Language", "Simple Query Language", "Standard Query Language", "Sequential Query Language", "A"),
    
    ("Which data type is used for a variable that can hold text in MySQL?", 
     "TEXT", "STRING", "CHAR", "VARCHAR", "D"),
    
    ("What is the purpose of the JOIN clause in MySQL?", 
     "To combine rows from two or more tables", "To filter data", "To sort data", "To create a new table", "A"),
    
    ("Which MySQL statement is used to update existing data in a table?", 
     "MODIFY", "UPDATE", "CHANGE", "SET", "B"),
    
    ("What is the default port number for MySQL server?", 
     "5432", "3306", "8080", "1521", "B"),
]


# Insert sample data into the DS3860 table
for q in questions:
    insert_question(*q)

print("Questions have been inserted into the DS3860 table.")

# Close the connection
conn.close()
