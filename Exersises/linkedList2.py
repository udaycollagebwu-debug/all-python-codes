class Empty:
    print("The stack is empty !")


class linkedStack:
    
    class Node:
        # __slots__ = 'data','next'
        def __init__(self,data,next):   
            self.data = data
            self.next = next
        # a node is inisiyalixe .
    
    def __init__(self):
        self.head = None
        self.size = 0
        # empyt stack 
    
    def is_empty(self):
        return self.size == 0
    def push(self,data):
        self.head = self.Node(data,self.head)
        self.size += 1
    
    def top(self):
        if self.is_empty():
            raise Empty('The stack is empty')
        return self.head.data
    def pop(self):
        if self.is_empty():
            raise Empty('The stack is empty !')
        ans =self.head.data
        self.head = self.head.next
        self.size -= 1
        return ans
    
    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

node = linkedStack()
# node.push(10)
# node.push(20)
# node.push(30)
# node.push(40)
# node.push(50)
node.display()

