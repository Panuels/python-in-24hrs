import sqlite3

# Step 1: Connect to a database (or create one if it doesn't exist)
connection = sqlite3.connect('example.db')

# Step 2: Create a cursor object to interact with the database
cursor = connection.cursor()

# Step 3: Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
)
''')

# Step 4: Insert data into the table
cursor.execute('''
INSERT INTO users (name, age) VALUES (?, ?)
''', ('Alice', 30))

cursor.execute('''
INSERT INTO users (name, age) VALUES (?, ?)
''', ('Bob', 25))

# Commit the changes
connection.commit()

# Step 5: Query the database
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)  # Output: (1, 'Alice', 30), (2, 'Bob', 25)

# Step 6: Close the connection
connection.close()
