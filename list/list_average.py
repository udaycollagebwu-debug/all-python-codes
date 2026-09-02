#calculete the average of the list
number_list=[]
#this is the empty list 
size=int(input("Enter the size of the number list :"))
#this is for the size of the list 
for i in range(size):
    list_element=int(input(f"Enter the list {i+1} element :"))
    number_list.append(list_element)      #this line is for storing the input into the list 
sumOfList=0
for i in range(size):
    sumOfList+=number_list[i]
average=sumOfList/size
print("The average of the number list is :",average)