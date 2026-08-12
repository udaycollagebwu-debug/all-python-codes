tuple_in = ('name',45)
print(type(tuple_in))
num_tu = (12,4,5,64,78,23,44)
print(num_tu.count(64))
print(num_tu.index(5))
a = (1,2,3,4,5,6,7)
b = ('a','b','c','d','e','f','g')
c = (a,b) # 2 D tuple 
print(c)
print(type(c))

print(c[0][0],c[1][2])