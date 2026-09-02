#Write a Python program that:
#Takes a list of numbers.
# Finds the maximum and minimum values.
# Calculates the sum of all elements.

#this are the quations and ia ma sdding a new challange that is i will do every think in function
def bigNum(list):
    resultBigNumber=max(list)
    return resultBigNumber
def smallNum(list):
    resultSmallNumber=min(list)
    return resultSmallNumber
def sumOfAll(list):
    resultSumOfAllNumbers=sum(numberList)
    return resultSumOfAllNumbers
numberList=[]
size=int(input("Enter the siz of the list (mins how many nubers you want to stare ): "))
for i in range(size):
    number=int(input(f"Enter the {i+1} element / number :"))
    numberList.append(number)
print("The list is :",numberList)
print("The biggest number of the list is :",bigNum(numberList))
print("The smallest number of the list is :",smallNum(numberList))
print("The sun of all number of the list is :",sumOfAll(numberList))