# take number input and factorial of the number 
number = int(input("Enter the number :"))
result=1
for i in range(1,number+1,1):
    result*=i
print("The factorial of the number ",number," is ",result)