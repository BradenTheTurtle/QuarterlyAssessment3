import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Create a table named DS3850 to store questions and answers
cursor.execute('''
CREATE TABLE IF NOT EXISTS DS3850 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL
)
''')

# Function to insert a question into the DS3850 table
def insert_question(question, option_a, option_b, option_c, option_d, correct_answer):
    cursor.execute('''
    INSERT INTO DS3850 (question, option_a, option_b, option_c, option_d, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (question, option_a, option_b, option_c, option_d, correct_answer))
    conn.commit()

# Questions in DB
questions = [
    ("What is the correct syntax to output 'Hello, World' in Python?", 
     "echo('Hello, World')", "print('Hello, World')", "console.log('Hello, World')", "printf('Hello, World')", "B"),
    
    ("Which of the following is a correct variable name in Python?", 
     "1variable", "variable_name", "variable-name", "var name", "B"),
    
    ("Which keyword is used to create a function in Python?", 
     "function", "def", "fun", "define", "B"),
    
    ("What will be the output of the following code? \n\nprint(type(3))",
     "<class 'float'>", "<class 'int'>", "<class 'str'>", "<class 'bool'>", "B"),
    
    ("Which of the following is not a Python data type?",
     "list", "dictionary", "tuple", "array", "D"),
    
    ("How do you insert comments in Python code?",
     "// This is a comment", "/* This is a comment */", "# This is a comment", "<!-- This is a comment -->", "C"),
    
    ("What is the output of this code? \n\nx = [1, 2, 3]\nprint(len(x))",
     "1", "2", "3", "4", "C"),
    
    ("What will be the output of this code? \n\nprint(10 // 3)",
     "3.33", "3", "3.0", "Error", "B"),
    
    ("Which method can be used to convert a string to lowercase in Python?", 
     "lower()", "tolowercase()", "strtolower()", "toLowerCase()", "A"),
    
    ("Which of the following operators is used for exponentiation in Python?", 
     "^", "**", "//", "exp()", "B"),
    
    ("What does the 'len' function do in Python?",
     "Finds the length of a string", "Calculates the sum of numbers", "Converts to lowercase", "Rounds a number", "A"),
    
    ("What is the output of this code? \n\nx = 'Hello'\nprint(x[1])",
     "H", "e", "l", "o", "B"),
    
    ("What is the result of '5 + 3 * 2' in Python?", 
     "11", "16", "13", "10", "A"),
    
    ("Which of these is the correct syntax to open a file named 'file.txt' in read mode?", 
     "open('file.txt')", "open('file.txt', 'r')", "open('file.txt', 'read')", "open('file.txt', 'w')", "B"),
    
    ("Which function is used to generate random numbers in Python?", 
     "randomize()", "rand()", "random()", "generate_random()", "C"),
    
    ("Which module provides support for regular expressions in Python?", 
     "re", "regex", "exp", "expressions", "A"),
    
    ("Which of the following statements will check if 'x' is equal to 'y'?", 
     "x = y", "x == y", "x != y", "x equal y", "B"),
    
    ("What is the default return value of a function that doesn't return anything explicitly?", 
     "0", "None", "null", "Undefined", "B"),
    
    ("Which of the following can be used to handle exceptions in Python?", 
     "try/except", "catch/try", "handle/error", "throw/catch", "A"),
    
    ("Which loop is best to use when you know the exact number of iterations needed?", 
     "while loop", "for loop", "do-while loop", "None of the above", "B"),
]

    # Add more questions here as needed

# Insert sample data into the DS3850 table
for q in questions:
    insert_question(*q)

print("Questions have been inserted into the DS3850 table.")

# Close the connection
conn.close()
