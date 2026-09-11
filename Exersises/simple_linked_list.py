class Empty(Exception):
   pass

class Linked_Stack:
    
    class Node:
        def __init__(self,data,next):
            self.data = data;
            self.next = next
    
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def push(self,data):
        self.head = self.Node(data,self.head)
        self.size += 1
    
    def top(self):
        if self.is_empty():
            raise Empty("The stack is empty !")
        return self.head.data
    
    def display(self):
        if self.is_empty():
            raise Empty("The stack is empty !")
        
        values = []
        element = self.head
        while element != None:
            values.append(element.data)
            element = element.next
        return values

node = Linked_Stack()
# node.push(10)
# node.push(20)
# node.push(30)
# node.push(40)
# node.push(50)
# node.push(60)
print("Whoud you like to add numbers in the stack ?")
print("------------------Yes / No------------------")
desaction = input("Enter you choice :")
if desaction.lower() == 'yes':
    count_number = int(input("Enter the count of the element you enter :"))
    for _ in range(count_number):
        number = int(input("Enter a number :"))
        node.push(number)     
elif desaction.lower() == 'no':
    print("Thanks you !")
else:
    print("You enterd a rong input !!")


try:
    values_return = node.display()
    print(values_return)
except Empty as error:
    print(error)