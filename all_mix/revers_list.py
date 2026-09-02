#Write a Python program to reverse a list without using reverse() or slicing
cars=[] #creat a empty list that holdes the cars names 
size=int(input("Enter the size of the list of cars :"))

for i in range(size):
    car_name=input(f"Enter the{i+1} car name :")  #it will take input of the names of the cars one by one 
    cars.append(car_name)

# reverse the list 
names=size-1
rev_cars=[]
while names >=0:
    rev_cars.append(cars[names])
    names-=1

# print the revers and the input list
print("The input list is :",cars)
print("The revers list is :",rev_cars)