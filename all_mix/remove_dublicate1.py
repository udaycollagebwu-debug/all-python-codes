numbers=[]  # this i a empty list ceerated .
remoed_dublicates=[]
size=int(input("Enter the size of the list : "))
for _ in range(size):
    numbers.append(int(input("Enter a value :"))) #this will take input every integer element dublicate also

remoed_dublicates = list(set(numbers))

print("The number list with dublicats : ",numbers)
print("The number list with no dublicates : ",remoed_dublicates)