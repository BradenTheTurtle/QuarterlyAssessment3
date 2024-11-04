import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Create a table named DS2810 to store questions and answers
cursor.execute('''
CREATE TABLE IF NOT EXISTS DS2810 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL
)
''')

# Function to insert a question into the DS2810 table
def insert_question(question, option_a, option_b, option_c, option_d, correct_answer):
    cursor.execute('''
    INSERT INTO DS2810 (question, option_a, option_b, option_c, option_d, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (question, option_a, option_b, option_c, option_d, correct_answer))
    conn.commit()

# Questions in DB
questions = [
    ("What is the file extension for an Excel workbook?", 
     ".xls", ".xlsx", ".xlsm", ".xlsb", "B"),
    
    ("Which Excel function is used to find the minimum value in a range?", 
     "MIN()", "LOWEST()", "MINIMUM()", "LEAST()", "A"),
    
    ("What is the shortcut to save a workbook in Excel?", 
     "Ctrl + S", "Ctrl + P", "Alt + S", "Shift + S", "A"),
    
    ("What feature allows you to automatically fill cells with data based on a pattern?", 
     "AutoFill", "Flash Fill", "Fill Handle", "Data Series", "C"),
    
    ("Which formula would you use to add up a range of cells?", 
     "ADD()", "SUM()", "TOTAL()", "SUMIF()", "B"),
    
    ("What does the VLOOKUP function do?", 
     "Looks up a value vertically in a table", "Calculates the average", 
     "Counts the number of cells", "Finds the maximum value", "A"),
    
    ("Which option is used to format cells in Excel?", 
     "Cell Styles", "Format as Table", "Conditional Formatting", "All of the above", "D"),
    
    ("How can you freeze panes in an Excel worksheet?", 
     "View > Freeze Panes", "Data > Freeze", "Layout > Freeze Rows", "Home > Freeze", "A"),
    
    ("What function would you use to concatenate text from two cells?", 
     "JOIN()", "CONCATENATE()", "MERGE()", "TEXTJOIN()", "B"),
    
    ("Which symbol is used to start a formula in Excel?", 
     "=", ":", "+", "#", "A"),
]




# Insert sample data into the DS2810 table
for q in questions:
    insert_question(*q)

print("Questions have been inserted into the DS2810 table.")

# Close the connection
conn.close()
