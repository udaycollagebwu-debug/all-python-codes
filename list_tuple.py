# The list ,tuple in this code 
list_provide=["uday","deba","nabayan",6,90]
tuple_provide=("uday","nabayan",78,90,45)
print(list_provide)
print(tuple_provide)
list_input=[]
tuple_input=()
for i in range(5):
    input_find=input(f"Enter a name or number for list{i+1}")
    list_input.append(input_find)
for i in range(5):
    input_find_tuple=input(f"Enter a name or a number for tuple {i+1}:")
    tuple_input = tuple_input + (input_find_tuple,)
print(list_input)
print(tuple_input)