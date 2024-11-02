# Question: Write a Python program that:

# Allows the user to input multiple student names and their grades 
# (stored as a comma-separated string of grades) and adds them to a dictionary.
# Then, lets the user look up any student’s grades by entering their name.
# If the student is not found in the dictionary, display a message saying, "Student not found."

# Example Interaction:
# Enter the student's name: Njeri
# Enter Njeri's grades (comma-separated): A, B+, B
# Do you want to add another student? (yes/no): yes

# Enter the student's name: Chets
# Enter Chets's grades (comma-separated): B, B-, C+
# Do you want to add another student? (yes/no): no

# Enter the name of the student to look up their grades: Njeri
# Njeri's grades are: A, B+, B
# This question will give you more practice working with dictionaries,
# loops, and user input handling in Python. Let me know if you'd like some hints!

# students = {
#     "vero": "A",
#     "charles": "A-",
#     "waweru": "B+",
#     "speczo": "B",
#     "nyams": "C"
# }
# students_name = input("Enter name of students you want to look up: ")

# if students_name in students:
#     print(f"{students_name} grades is {students[students_name]}")
# else:
#     print("student not found")
    
students = {
    "vero": "A",
    "charles": "A-",
    "waweru": "B+",
    "speczo": "B",
    "nyams": "C"
}

while True:
    # Prompt for the student name
    students_name = input("Enter the name of the student you want to look up: ").lower()

    # Check if the name is in the dictionary
    if students_name in students:
        print(f"{students_name.capitalize()}'s grade is {students[students_name]}")
    else:
        print("Student not found.")

    # Ask if the user wants to look up another student
    another = input("Do you want to look up another name? (yes/no): ").strip().lower()
    if another != "yes":
        print("Exiting the program.")
        break

