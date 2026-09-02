def sum_list_element(given_list, list_size):
    result=0
    for i in range(list_size):
        result+=given_list[i]
    return result

numb_list=[] #declear the list 
size =int (input("Enter the list size :"))
# take input from the user 
for i in range(size):
    list_element=int(input(f"Enter the list {i+1} element :"))
    numb_list.append(list_element)
print("The number list is :",numb_list)
return_value=sum_list_element(numb_list,size)
print("The sum of all elament is :", return_value)