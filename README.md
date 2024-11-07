# QuarterlyAssessment3

# addDataToDB.py file
    This Python script connects to an SQLite database (questions.db), creates a table called ECON3610 (if it doesn't exist), and inserts a set of sample quiz questions with multiple-choice options and correct answers. The table stores the question text, four options (A, B, C, D), and the correct answer. The script uses the sqlite3 library to perform these operations. Once run, it creates the database and populates it with sample questions, which can then be queried for use in a quiz application. The database is stored in the same directory as the script, and the table structure can be modified or expanded as needed. To use, simply run the script to set up the database.

# main.py file
    This Python script creates a graphical user interface (GUI) for a quiz application using the tkinter library. It connects to an SQLite database (questions.db), dynamically loads available quiz categories (tables), and allows the user to select a category to start the quiz. The script fetches the questions and answers from the selected category, presents them one by one in a new quiz window, and provides radio buttons for answering. After the user submits an answer, the script checks if the selected answer is correct and proceeds to the next question. Once all questions are answered, a message box displays a "Quiz Complete" message. The sqlite3 library is used to interact with the database, and the script filters out the sqlite_sequence table from the list of categories.

# readDB.py file
    This Python script connects to an SQLite database (questions.db), retrieves and displays a list of all tables in the database, and allows the user to select a table to view. After the user selects a table, the script fetches and prints all the data from that table, including column headers and row values. The script uses the sqlite3 library to interact with the database. It first lists the table names, then prompts the user to choose a table by its index. Finally, it retrieves and prints the data in a tabular format. This tool is useful for inspecting the contents of a database directly from the command line.

# questions.db file
    This is the database that houses all the questions for the quizbowl.
