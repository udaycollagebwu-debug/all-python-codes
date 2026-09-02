# use some spectial operations ..

# for addition "a + b"

a = 10
b = 2

print("addition :")
print(a +b)
print("spactial :",a.__add__(b))

#for subtraction "a - b"
print("subtraction :")
print(a - b)
print("spectial :",a.__sub__(b))

# for mualtiplaction "a * b"
print("mualtiplaction :")
print(a * b)
print("spectial :",a.__mul__(b))

# for divesion " a / b"
print("division if true :")
print(a / b)
print("spectial :",a.__truediv__(b))

# for divesion " a // b"
print("division is floor :")
print(a // b)
print("spectial :",a.__floordiv__(b))

# for modulas "a % b"
print("modulas :")
print(a % b)
print("spectial :",a.__mod__(b))

# for power "a ** b"
print("power :")
print(a ** b)
print("spectial :",a.__pow__(b))

# for and operation 
c = True
d = False

print("and operation .")
print(c.__and__(d))

# for or operation 

print("or operation .")
print(c.__or__(d))