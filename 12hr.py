# importing modules  using inbuilt python modules like math, random 

# import math 
# print(math.sqrt(16))

# # ex1
# import math
# number = int(input("enter a number? "))
# print(math.sqrt(number))

import random
print(random.randint(1, 10))

# If `A` and `Z` are letters and you want to generate a random letter between them,
# you can use the `random.choice()` function from the `random` module.
# Here's how you can do that:
import random
# Define the range of letters
A = 'A'  # Starting letter
Z = 'Z'  # Ending letter

# Generate a random letter between A and Z (inclusive)
random_letter = random.choice([chr(i) for i in range(ord(A), ord(Z) + 1)])
print(random_letter)
# In this code:
# - `ord(A)` gets the Unicode code point of the letter `A`.
# - `ord(Z) + 1` gets the code point of `Z` plus one, making the range inclusive.
# - `chr(i)` converts the Unicode code point back to a character.
# - `random.choice()` selects a random letter from the generated list of letters. 
# This will print a random uppercase letter between `A` and `Z`.

import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()  
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)')
conn.commit()
conn.close()