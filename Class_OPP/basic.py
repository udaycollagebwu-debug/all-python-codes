class student:
    def __init__(self,name,marks):    # what is __init__ : --> __init__ is a constructor that set up everything when the object is created
        self.name = name              # what is ' self ' : --> self is a identifire the help the class to know what is his object .this helpa the object to keep it's own data (value) if we creat mulltipal object in the same class .
        self.marks = marks
    def display(self):
        print("Student name is :",self.name,
              "\nStudent get the marks :",self.marks)


s1 = student("uday sankar singha",98)
s2 = student("riya singha",88)

s1.display()
s2.display()