#take a empty list input .
numb_list=[]
#then take the input from the user 
size=int(input("Enter the size of the list :"))
for i in range(size):
    element=int(input(f"Enter the element of the list {i+1} number : "))
    numb_list.append(element)
    #now the list is stored. 
# print(numb_list) 
result=0
for i in range(size):
    result+=numb_list[i]  #this is for the sum [ take each of the element and do the sum]
print("The list of number is :",numb_list) #display the result 
print("The sum of all element from the list is :",result)