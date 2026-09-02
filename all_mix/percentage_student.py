percentage = float(input("Enter the percentage of marks obtained: "))
if percentage >=60:
    print("Grade: First Class")
elif 50 <= percentage < 60:
    print("Grade: Second Class")
elif 40 <= percentage < 50:
    print("Grade: Third Class")
else:
    print("Grade: Fail")
