# Store student names as keys and their marks as values. Print the name of the student with the highest marks.

student_details = {} # this is a empty dictionary

size = int(input("Enter how many student you store in the dectionary :"))

# to store the student details in the dectionary
for _ in range(size):
    name = input("Enter name :")
    marks = float(input("Enter the marks :"))
    student_details[name] = marks

top_student = max(student_details,key=student_details.get)

print("The top scorrer in the dictionary is :",top_student)