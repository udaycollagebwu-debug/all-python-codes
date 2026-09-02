#calculate the area of the tringale 
side1=float(input("Enter the first side of the tringale :"))
side2=float(input("Enter the second side of the tringale :"))
side3=float(input("Enter the therd side of the tringale :"))

s=(side1+side2+side3)/2
area=(s*(s-side1)*(s-side2)*(s-side3))**0.5
print("the arear is :",area)