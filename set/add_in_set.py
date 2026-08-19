name = {'uday','sankar','sibam','kumar'}

print(name)

name.add("deba")  # we can add eliment in the set 
print(name)

#we can't axces the set becaus the set is changeng the elements continuasly 

name_list = list(name)
name_list[3]= "nabayan"
name = set(name_list)  

print(name)
print(type(name))