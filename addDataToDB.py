import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Create a table named LAW2810 to store questions and answers
cursor.execute('''
CREATE TABLE IF NOT EXISTS LAW2810 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL
)
''')

# Function to insert a question into the LAW2810 table
def insert_question(question, option_a, option_b, option_c, option_d, correct_answer):
    cursor.execute('''
    INSERT INTO LAW2810 (question, option_a, option_b, option_c, option_d, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (question, option_a, option_b, option_c, option_d, correct_answer))
    conn.commit()

# Questions in DB
questions = [
    ("What is the primary purpose of contract law?", 
     "To regulate business transactions", "To enforce agreements", 
     "To protect consumers", "To set prices", "B"),
    
    ("Which of the following is an essential element of a valid contract?", 
     "Offer", "Acceptance", "Consideration", "All of the above", "D"),
    
    ("What term refers to the legal ability to enter into a contract?", 
     "Capacity", "Legitimacy", "Authority", "Competence", "A"),
    
    ("Which type of contract must be in writing to be enforceable?", 
     "Verbal contracts", "Implied contracts", "Contracts for the sale of goods over a certain amount", "Informal contracts", "C"),
    
    ("What is the term for an agreement that is not legally enforceable?", 
     "Void contract", "Valid contract", "Breach of contract", "Executed contract", "A"),
    
    ("Which of the following is a defense to breach of contract?", 
     "Impossibility", "Negligence", "Mistake", "All of the above", "A"),
    
    ("What does tort law deal with?", 
     "Criminal offenses", "Civil wrongs", "Contractual disputes", "Business regulations", "B"),
    
    ("What is the legal term for the transfer of property ownership?", 
     "Assignment", "Delegation", "Conveyance", "Subrogation", "C"),
    
    ("Which of the following entities provides limited liability protection to its owners?", 
     "Sole proprietorship", "Partnership", "Corporation", "General partnership", "C"),
    
    ("What does the term 'due diligence' refer to in business law?", 
     "The process of legal compliance", "The investigation of a business before a transaction", 
     "The negotiation of contract terms", "The enforcement of laws", "B"),
]



# Insert sample data into the DS3860 table
for q in questions:
    insert_question(*q)

print("Questions have been inserted into the LAW2810 table.")

# Close the connection
conn.close()
