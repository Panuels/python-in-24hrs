# write a program that scores three students and their grades in a dictionary . 
# Allow the user to look up a students by entering their name

grades = {"Njeri": "A, A-, B", "chets":"B, B+, B-", "panny":"B, C+, C"}
print(grades["Njeri"])


# complex answer
# Dictionary to store student names and their grades
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

# Prompt the user to enter a student's name to look up their grade
student_name = input("Enter the name of the student to look up their grade: ")

# Check if the student's name is in the dictionary
if student_name in students:
    print(f"{student_name}'s grade is: {students[student_name]}")
else:
    print("Student not found.")

