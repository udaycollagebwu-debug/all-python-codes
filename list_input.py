numberList=[]
reng=int (input("Enter how many numbers you  want to store :"))
for i in range(reng):
    num=int(input(f"Enter the number for storing in the list {i+1}:"))
    numberList.append(num)

print("Your list is :",numberList)