# grading system
grade = int(input("what is your overall grade? "))

if grade >90:
    print("you did excellent. Thats an A.")
elif 80<= grade <=90:
    print("you did the best. Thats a B.") 
elif 50<= grade <80:
    print("try harder next time. Thats a C.")
elif 20<= grade <50:
    print("There is always room for improvement. Thats a D. ")
else :
    print("You Failed.")
    
    # results

# what is your overall grade? 85
# you did the best. Thats a B.

# what is your overall grade? 60
# try harder next time. Thats a C.

# what is your overall grade? 35
# There is always room for improvement. Thats a D.

# what is your overall grade? 10
# You Failed.

# PASSED 