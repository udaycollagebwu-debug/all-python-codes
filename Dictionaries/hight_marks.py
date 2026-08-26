# Store student names as keys and their marks as values. Print the name of the student with the highest marks.

student_details = {} # this is a empty dictionary

size = int(input("Enter how many student you store in the dectionary :"))

for _ in range(size):
    name = input("Enter name :")
    marks = float(input("Enter the marks :"))
    student_details[name] = marks


print(student_details)
print(type(student_details))
