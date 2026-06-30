name_list=['uday','raja','nabayan','ashok','radhika','balika','riya','nandani','daymonti','bidhut']
print("The name list is :",name_list)
print("print the name using the for loop :")
for x in name_list:
    print(x)
print("The name has any 'y':")
for x in name_list:
    if 'y' in x:
        print(x)
print("The list heve to short that why use the sort() function .")
name_list.sort()
print("The short list is :",name_list)
print ("The list in the revers order .")
name_list.sort(reverse=True)
print("The revers order list is :",name_list)