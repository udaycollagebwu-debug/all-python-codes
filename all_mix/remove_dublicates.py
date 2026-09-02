# How do you remove duplicates from a list?
numbers=[]  # this i a empty list ceerated .
remoed_dublicates=[]
size=int(input("Enter the size of the list : "))
for _ in range(size):
    numbers.append(int(input("Enter a value :"))) #this will take input every integer element dublicate also

# for removing the dublicates 
for num in numbers:
    if num not in remoed_dublicates:
        remoed_dublicates.append(num)

print("The number list with dublicats : ",numbers)
print("The number list with no dublicates : ",remoed_dublicates)
    