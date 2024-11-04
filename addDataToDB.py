import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Create a table named ECON3610 to store questions and answers
cursor.execute('''
CREATE TABLE IF NOT EXISTS ECON3610 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL
)
''')

# Function to insert a question into the ECON3610 table
def insert_question(question, option_a, option_b, option_c, option_d, correct_answer):
    cursor.execute('''
    INSERT INTO ECON3610 (question, option_a, option_b, option_c, option_d, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (question, option_a, option_b, option_c, option_d, correct_answer))
    conn.commit()

# Questions in DB
questions = [
    ("What is the measure of central tendency that represents the average?", 
     "Median", "Mode", "Mean", "Range", "C"),
    
    ("Which of the following is a graphical representation of data distribution?", 
     "Pie chart", "Bar chart", "Histogram", "All of the above", "D"),
    
    ("What does a standard deviation indicate about a dataset?", 
     "The average value", "The spread of the data", "The highest value", "The lowest value", "B"),
    
    ("In a normal distribution, what percentage of data falls within one standard deviation of the mean?", 
     "68%", "75%", "95%", "99.7%", "A"),
    
    ("What is the purpose of a hypothesis test?", 
     "To confirm a theory", "To make inferences about a population", 
     "To analyze variance", "To collect data", "B"),
    
    ("Which term describes the midpoint of a data set when arranged in order?", 
     "Mean", "Mode", "Median", "Range", "C"),
    
    ("What is the likelihood of an event occurring called?", 
     "Probability", "Possibility", "Likelihood", "Chance", "A"),
    
    ("Which of the following measures the relationship between two variables?", 
     "Mean", "Correlation", "Variance", "Standard deviation", "B"),
    
    ("What type of sampling involves selecting every nth individual from a population?", 
     "Random sampling", "Stratified sampling", "Systematic sampling", "Cluster sampling", "C"),
    
    ("What is a common method to visualize the relationship between two quantitative variables?", 
     "Bar chart", "Pie chart", "Scatter plot", "Histogram", "C"),
]



# Insert sample data into the ECON3610 table
for q in questions:
    insert_question(*q)

print("Questions have been inserted into the ECON3610 table.")

# Close the connection
conn.close()
