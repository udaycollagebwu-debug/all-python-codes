def primeNumber(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
num=int(input("Enter the nuber that you want to check the prime number :"))
result=primeNumber(num)
if result== False:
    print("The number is not a Prime Number .")
else:
    print("The number is a Prime number .")