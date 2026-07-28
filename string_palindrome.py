string = input("Enter a string :")
revers_string = string[::-1]
print("The original string is :",string)
print("The revers code is :",revers_string)
if revers_string == string:
    print("The string is a palindrme string .")
else:
    print("The string is not a palindrome string !")