#reverse number (print a number in reverse order)
number =int(input("Enter a number : "))
revers=0
original=number
while number!=0:
    remincder=number%10
    revers=revers*10+remincder
    number=number//10 #this will gives us the output of integer .
print("The reverse number is :",revers)
if(revers==original):
    print("The number is a palindrome number !")